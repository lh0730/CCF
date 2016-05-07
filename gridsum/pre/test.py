# -*- coding: utf8 -*-
import sys
import re
from preprocess import pre

reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    test_str = u'二、变更上海市浦东新区人民法院（2013）浦民一（民）初字第30748号民事判决第十三项为：上述第四、七、八、九、十项，于本判决生效之日起十日内，由傅甲支付阎丙37，655.50元、姚丁37，655.50元、阎乙96，919.90元，合计172，230.90元（减去已支付的113，500元，实际应支付五万八千七百元九角）。'
    print test_str
    print pre(test_str)
