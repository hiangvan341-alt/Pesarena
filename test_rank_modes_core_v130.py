from modules.rank_modes import service

def setup_module(): service.configure({})
def player(rp, matches): return {'rating':rp,'total_matches':matches}
def test_unlocks():
 assert service.check_rank_mode_eligibility('rank_random',player(1000,0))['eligible']
 assert not service.check_rank_mode_eligibility('random3_pick1',player(1000,4))['eligible']
 assert service.check_rank_mode_eligibility('random3_pick1',player(1000,5))['eligible']
 assert service.check_rank_mode_eligibility('bo3',player(1300,15),player(1600,20))['eligible']
 assert not service.check_rank_mode_eligibility('bo3',player(1300,15),player(1900,20))['eligible']
def test_bo3_results_and_rp():
 games=[{'winner_side':'player1'},{'winner_side':'player1'}]
 result=service.resolve_series_result('bo3',games)
 assert result['status']=='completed' and result['score']=='2-0'
 assert service.calculate_mode_rp('bo3',result,'player1')=={'winner':40,'loser':-28,'key':'2-0'}
def test_home_away_aggregate():
 result=service.resolve_series_result('home_away',[{'player1_score':1,'player2_score':0,'winner_side':'player1'},{'player1_score':0,'player2_score':2,'winner_side':'player2'}])
 assert result['aggregate_score']=='1-2' and result['winner_side']=='player2'
def test_forfeit_not_clean_2_0_bonus():
 result=service.resolve_series_result('tactical_bo3',[],forfeiting_user_id='u1')
 rp=service.calculate_mode_rp('tactical_bo3',result,'player2',True)
 assert rp=={'winner':34,'loser':-32,'key':'forfeit'}
