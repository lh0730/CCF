# -*- coding: utf8 -*-
__author__ = 'Tan'

import sys
from hanzi import hanzi
from douhao import douhao
from baifenhao import baifenhao
from nianyueri import nianyueri
from dangdelete import dangdelete
from wanyuan import wanyuan


reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    test_str =u'''"据此，依照《中华人民共和国担保法》第十八条，最高人民法院关于适用《中华人民共和国担保法》若干问题的解释第二十三条及《中华人民共和国民事诉讼法》第一百七十条第一款第（二）项及第一百七十五条之规定，判决如下：
一、维持上海市浦东新区人民法院（2014）浦民六（商）初字第6604号民事判决第一项，即被上诉人上海三毛进出口有限公司应于本判决生效之日起十日内归还上诉人中信银行股份有限公司上海分行押汇金额9，644，014.96美元；
二、维持上海市浦东新区人民法院（2014）浦民六（商）初字第6604号民事判决第二项，即被上诉人上海三毛进出口有限公司应于本判决生效之日起十日内偿付上诉人中信银行股份有限公司上海分行至2014年5月23日止的逾期付款利息191，729.26美元，并自2014年5月24日起至实际清偿日止分别按约定利率偿付逾期利息，其中6，636，910.96美元按1.905%计算、1，531，104美元按1.303%计算、1，476，000美元按1.304%计算；
三、撤销上海市浦东新区人民法院（2014）浦民六（商）初字第6604号民事判决第三项；
四、被上诉人上海三毛企业（集团）股份有限公司对被上诉人上海三毛进出口有限公司上述还款义务在人民币6，000万元最高额内承担连带担保责任。被上诉人上海三毛企业（集团）股份有限公司承担全部责任后可依法向被上诉人上海三毛进出口有限公司追偿。
负有金钱给付义务的当事人如未按本判决指定的期间履行给付义务，应当按照《中华人民共和国民事诉讼法》第二百五十三条之规定，加倍支付迟延履行期间的债务利息。"
'''

    print test_str
    test_str = hanzi(test_str)
    test_str = douhao(test_str)
    test_str = baifenhao(test_str)
    test_str = nianyueri(test_str)
    test_str = dangdelete(test_str)
    test_str = wanyuan(test_str)
    print test_str