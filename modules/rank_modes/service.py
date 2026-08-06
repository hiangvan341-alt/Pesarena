import json
from copy import deepcopy
from .catalog import DEFAULT_MODE_CONFIGS, MODE_ORDER, RANK_RANDOM, RANDOM3_PICK1
_CONTEXT={}; SETTING_KEY='rank_mode_configs_v1'
EXPORTED_NAMES=('save_rank_mode_configs','get_rank_mode_configs','get_rank_mode','rank_mode_catalog_for_players','check_rank_mode_eligibility','rank_mode_eligibility_for_room','get_user_rank_mode_unlocks','list_rank_mode_user_unlocks','save_user_rank_mode_unlocks','resolve_series_result','calculate_mode_rp','is_series_mode','legacy_team_tier_for_mode','normalize_rank_mode_code','MODE_ORDER','RANK_RANDOM','RANDOM3_PICK1')
def configure(context):
 global _CONTEXT; _CONTEXT=context
def _deep_merge(base, override):
 r=deepcopy(base)
 for k,v in (override or {}).items(): r[k]=_deep_merge(r[k],v) if isinstance(v,dict) and isinstance(r.get(k),dict) else v
 return r
def normalize_rank_mode_code(value):
 value=str(value or '').strip().lower(); return {'smart_random':RANK_RANDOM,'random':RANK_RANDOM}.get(value,value if value in DEFAULT_MODE_CONFIGS else RANK_RANDOM)

def save_rank_mode_configs(configs):
 clean={}
 for code in MODE_ORDER:
  incoming=(configs or {}).get(code) or {}
  clean[code]=_deep_merge(DEFAULT_MODE_CONFIGS[code],incoming)
 execute_query=_CONTEXT.get('execute_query'); db=_CONTEXT.get('db')
 if not execute_query or db is None: raise RuntimeError('Database chưa sẵn sàng')
 payload={'setting_key':SETTING_KEY,'setting_value':json.dumps(clean,ensure_ascii=False)}
 execute_query(db.table('system_settings').upsert(payload,on_conflict='setting_key'),'save_rank_mode_configs',attempts=2)
 return clean

def get_rank_mode_configs():
 configs=deepcopy(DEFAULT_MODE_CONFIGS); execute_query=_CONTEXT.get('execute_query'); db=_CONTEXT.get('db')
 if not execute_query or db is None: return configs
 try:
  result=execute_query(db.table('system_settings').select('setting_value').eq('setting_key',SETTING_KEY).limit(1),'get_rank_mode_configs',attempts=1)
  raw=((result.data or [{}])[0]).get('setting_value'); raw=json.loads(raw) if isinstance(raw,str) else raw
  if isinstance(raw,dict):
   for code in MODE_ORDER:
    if isinstance(raw.get(code),dict): configs[code]=_deep_merge(configs[code],raw[code])
 except Exception: pass
 return configs
def get_rank_mode(code): return get_rank_mode_configs()[normalize_rank_mode_code(code)]


def _is_admin_account(user):
 is_admin_user=_CONTEXT.get('is_admin_user')
 if callable(is_admin_user):
  try: return bool(is_admin_user(user))
  except Exception: pass
 return bool(user and (user.get('role')=='admin' or user.get('admin_level')))

def get_user_rank_mode_unlocks(user_id):
 """Trả về tập mã chế độ được Admin mở riêng cho một tài khoản."""
 if not user_id: return set()
 execute_query=_CONTEXT.get('execute_query'); db=_CONTEXT.get('db')
 if not execute_query or db is None: return set()
 cache_key=f'rank_mode_unlocks:{user_id}'
 has_request_context=_CONTEXT.get('has_request_context'); g=_CONTEXT.get('g')
 if callable(has_request_context) and has_request_context() and g is not None:
  cache=getattr(g,'_rank_mode_unlock_cache',None)
  if cache is None:
   cache={}; setattr(g,'_rank_mode_unlock_cache',cache)
  if cache_key in cache: return set(cache[cache_key])
 try:
  result=execute_query(db.table('rank_mode_user_unlocks').select('mode_code').eq('user_id',user_id).eq('is_unlocked',True),'get_user_rank_mode_unlocks',attempts=1)
  modes={normalize_rank_mode_code(row.get('mode_code')) for row in (result.data or []) if row.get('mode_code') in DEFAULT_MODE_CONFIGS}
 except Exception:
  modes=set()
 if callable(has_request_context) and has_request_context() and g is not None:
  getattr(g,'_rank_mode_unlock_cache',{})[cache_key]=set(modes)
 return modes

def list_rank_mode_user_unlocks():
 execute_query=_CONTEXT.get('execute_query'); db=_CONTEXT.get('db')
 if not execute_query or db is None: return {}
 try:
  result=execute_query(db.table('rank_mode_user_unlocks').select('user_id,mode_code,is_unlocked').eq('is_unlocked',True),'list_rank_mode_user_unlocks',attempts=1)
 except Exception:
  return {}
 output={}
 for row in (result.data or []):
  user_id=str(row.get('user_id') or '')
  code=str(row.get('mode_code') or '')
  if user_id and code in DEFAULT_MODE_CONFIGS: output.setdefault(user_id,set()).add(code)
 return output

def save_user_rank_mode_unlocks(user_id, mode_codes, updated_by=None):
 execute_query=_CONTEXT.get('execute_query'); db=_CONTEXT.get('db')
 if not execute_query or db is None: raise RuntimeError('Database chưa sẵn sàng')
 valid=[code for code in MODE_ORDER if code in set(mode_codes or [])]
 execute_query(db.table('rank_mode_user_unlocks').delete().eq('user_id',user_id),'delete_user_rank_mode_unlocks',attempts=2)
 if valid:
  rows=[{'user_id':user_id,'mode_code':code,'is_unlocked':True,'updated_by':updated_by} for code in valid]
  execute_query(db.table('rank_mode_user_unlocks').insert(rows),'save_user_rank_mode_unlocks',attempts=2)
 return set(valid)

def _completed_rank_matches(user):
 user=user or {}
 # Dữ liệu chuẩn của PES Arena là tổng W/H/B. Ưu tiên nguồn này để tránh
 # total_matches cũ/chưa đồng bộ làm khóa sai chế độ.
 if any(key in user for key in ('wins','draws','losses')):
  try:
   return max(0,int(user.get('wins') or 0)+int(user.get('draws') or 0)+int(user.get('losses') or 0))
  except (TypeError,ValueError):
   pass
 for key in ('total_matches','matches_played','rank_matches','completed_matches'):
  try:
   value=int(user.get(key) or 0)
   if value: return value
  except (TypeError,ValueError): pass
 return 0
def check_rank_mode_eligibility(mode_code,user,opponent=None):
 mode_code=normalize_rank_mode_code(mode_code); mode=get_rank_mode(mode_code); reasons=[]
 if not mode.get('enabled',True): reasons.append('Chế độ đang tạm tắt')
 user=user or {}
 admin_unlocked=_is_admin_account(user)
 manual_unlocked=mode_code in get_user_rank_mode_unlocks(user.get('id'))
 bypass_requirements=admin_unlocked or manual_unlocked
 user_rp=int(user.get('rank_points') or user.get('rating') or user.get('rp') or 0); min_rp=int(mode.get('min_rp') or 0)
 if not bypass_requirements and user_rp<min_rp: reasons.append(f'Cần tối thiểu {min_rp:,} RP'.replace(',','.'))
 played=_completed_rank_matches(user); min_matches=int(mode.get('min_matches') or 0)
 if not bypass_requirements and played<min_matches: reasons.append(f'Cần hoàn thành {min_matches} trận Rank')
 max_gap=int(mode.get('max_rp_gap') or 0)
 if opponent and max_gap>0:
  opponent_rp=int((opponent or {}).get('rank_points') or (opponent or {}).get('rating') or (opponent or {}).get('rp') or 0)
  if abs(user_rp-opponent_rp)>max_gap: reasons.append(f'Hai người không được chênh quá {max_gap} RP')
 return {'eligible':not reasons,'reasons':reasons,'mode':mode,'admin_unlocked':admin_unlocked,'manual_unlocked':manual_unlocked}
def rank_mode_eligibility_for_room(mode_code,host,guest=None):
 h=check_rank_mode_eligibility(mode_code,host,guest); g=check_rank_mode_eligibility(mode_code,guest,host) if guest else {'eligible':True,'reasons':[]}; reasons=list(h['reasons'])
 for x in g['reasons']:
  if x not in reasons: reasons.append(x)
 return {'eligible':h['eligible'] and g['eligible'],'reasons':reasons}
def rank_mode_catalog_for_players(host,guest=None):
 return [{**get_rank_mode(c),**{'eligible':rank_mode_eligibility_for_room(c,host,guest)['eligible'],'lock_reasons':rank_mode_eligibility_for_room(c,host,guest)['reasons']}} for c in MODE_ORDER]
def is_series_mode(mode_code): return get_rank_mode(mode_code).get('series_type')!='single'
def legacy_team_tier_for_mode(mode_code): return 'smart_random' if normalize_rank_mode_code(mode_code)==RANK_RANDOM else normalize_rank_mode_code(mode_code)
def resolve_series_result(mode_code,games,forfeiting_user_id=None):
 mode=get_rank_mode(mode_code); clean=[g for g in (games or []) if g.get('status','completed')=='completed']; p1=sum(g.get('winner_side')=='player1' for g in clean); p2=sum(g.get('winner_side')=='player2' for g in clean); draws=sum(g.get('winner_side')=='draw' for g in clean)
 if forfeiting_user_id: return {'status':'completed','reason':'forfeit','forfeiting_user_id':forfeiting_user_id,'score':'0-2','p1_wins':p1,'p2_wins':p2,'draws':draws}
 if mode.get('series_type')=='aggregate_two_legs':
  if len(clean)<2:return {'status':'playing','p1_wins':p1,'p2_wins':p2,'draws':draws}
  a=sum(int(g.get('player1_score') or 0) for g in clean[:2]); b=sum(int(g.get('player2_score') or 0) for g in clean[:2]); w='player1' if a>b else 'player2' if b>a else 'draw'; return {'status':'completed','reason':'aggregate','winner_side':w,'aggregate_score':f'{a}-{b}','p1_wins':p1,'p2_wins':p2,'draws':draws}
 req=int(mode.get('wins_required') or 2)
 if p1>=req or p2>=req:
  w='player1' if p1>p2 else 'player2'; return {'status':'completed','reason':'wins_required','winner_side':w,'score':f'{max(p1,p2)}-{min(p1,p2)}','p1_wins':p1,'p2_wins':p2,'draws':draws}
 if len(clean)>=int(mode.get('max_games') or 3):
  w='player1' if p1>p2 else 'player2' if p2>p1 else 'draw'; return {'status':'completed','reason':'max_games','winner_side':w,'score':f'{p1}-{p2}','p1_wins':p1,'p2_wins':p2,'draws':draws}
 return {'status':'playing','p1_wins':p1,'p2_wins':p2,'draws':draws}
def calculate_mode_rp(mode_code,series_result,winner_side=None,forfeit=False):
 mode=get_rank_mode(mode_code); rp=mode.get('rp') or {}
 if mode.get('series_type')=='single': return {'formula':'rank_current'}
 if forfeit or series_result.get('reason')=='forfeit': return {'winner':int(rp.get('forfeit_win') or 0),'loser':int(rp.get('forfeit_loss') or 0),'key':'forfeit'}
 if series_result.get('winner_side')=='draw' or not winner_side:
  key='draw_all' if int(series_result.get('draws') or 0)>=int(mode.get('max_games') or 3) else 'draw_1_1'; value=int(rp.get(key,rp.get('draw',0)) or 0); return {'player1':value,'player2':value,'key':key}
 score=str(series_result.get('score') or '')
 if score=='2-0': return {'winner':int(rp.get('win_2_0') or rp.get('win_both') or 0),'loser':int(rp.get('lose_0_2') or rp.get('lose_both') or 0),'key':'2-0'}
 return {'winner':int(rp.get('win_2_1') or rp.get('one_win_one_draw_win') or 0),'loser':int(rp.get('lose_1_2') or rp.get('one_win_one_draw_loss') or 0),'key':'2-1'}
