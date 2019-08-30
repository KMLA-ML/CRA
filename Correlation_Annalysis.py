# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/tjddbs0401/645761473da4d64e46b82b5ea12414c5/untitled3.ipynb
"""

import pandas as pd
xls = pd.read_excel("test_project.xlsx", index_col=0)

xls



corr_matrix = xls.corr()

corr_matrix["범죄율"].sort_values(ascending=False)



"""범죄율                       1.000000
노인 천명당 노인여가복지시설수 (개)      0.337681
합계출산율                     0.286010
인구 천명당 의료기관병상수 (개)        0.247788
인구증가율 (%)                 0.233469
독거노인가구비율 (%)              0.215378
논경지면적 (헥타르)               0.193084
고령인구비율 (%)                0.182359
인구 십만명당 문화기반시설수 (개)       0.166790
1인당 자동차 등록대수 (대)          0.130790
평균연령                      0.129331
주민 만명당 화재발생건수 (건)         0.117715
인구 십만명당 사회복지시설수 (개)       0.058538
스트레스 인지율 (%)              0.041981
비만율 (%)                   0.038753
인구십만명당 자살률 (십만명당)        -0.001621
재정자주도 (%)                -0.035380
대학교 수 (개)                -0.042108
요양기관수 (개)                -0.054494
대학교 학생수 (명)              -0.054585
조혼인율                     -0.063111
주민등록인구 (명)               -0.064495
화재발생건수 (건)               -0.065606
가구수                      -0.065767
건강보험 적용인구 현황             -0.066030
출생아수                     -0.066745
사망자수 (명)                 -0.066771
주택수 (호)                  -0.067621
사업체수 (개)                 -0.068283
초등학교 교원수 (명)             -0.070791
등록외국인 현황  (명)            -0.074406
초등학교 학생수 (명)             -0.074623
일반회계중 일반공공행정예산비중 (%)     -0.077395
초등학교수 (개)                -0.081853
유치원 원아수 (명)              -0.086653
유치원수 (개)                 -0.094389
폐수배출업소수 (개소)             -0.120295
유아 천명당 보육시설수 (개)         -0.124157
교원1인당 학생수 (명)            -0.128819
고위험음주율 (%)               -0.136667
음주율 (%)                  -0.138396
재정자립도 (%)                -0.160542
인구 천명당 외국인수 (명)          -0.175310
남녀성비 (%)                 -0.184414
하수도보급률 (%)               -0.193198
자동차 천대당 교통사고발생건수 (건)     -0.207803
주민 1인당 생활폐기물배출량 (kg/일)   -0.228728
인구 천명당 사설학원수 (개)         -0.231967
흡연율 (%)                  -0.243059
상수도보급률 (%)               -0.243113
일반회계중 사회복지예산비중 (%)       -0.253021
조이혼율                     -0.292742
"""