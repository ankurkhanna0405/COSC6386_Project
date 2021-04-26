def pass_fail(score1: int, score2: int, score3: int, score4: int) -> str:
   
    if (score1 + score2 + score3 + score4)/4 < 50:
        return "Fail"
    if (score1 + score2 + score3 + score4)/4 > 90:
        return "Pass, A grade"
    if (score1 + score2 + score3 + score4)/4 >80:
        return "Pass, B grade"
    if (score1 + score2 + score3 + score4)/4 >70:
         return "Pass, C grade"
    else:
        return "Pass, D grade"
