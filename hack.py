import os
old = open('registry.dat', 'r')
new = open('all.dat', 'w')
for line in old.readlines():
    if 'guld:Liabilities:' in line:
        pairdirty = line.replace('guld:Liabilities:', '').replace('guld', '').strip()
        mind = pairdirty.rfind('-')
        amount = pairdirty[mind-1:].replace('-', '').replace('guld', '').strip()
        print(amount)
        name = pairdirty[:mind-1].strip()
        try:
            os.makedirs('/home/tigopay/ledger/guld/%s' % name)
        except Exception:
            pass
        if True:#not os.path.exists('/home/tigopay/ledger/guld/%s/1496275200.dat' % name):
            pf = open('/home/tigopay/ledger/guld/%s/1496275200.dat' % name, 'w')
            pf.write('2016/06/01 * guld pre-founding contributions\n    mizim:Assets                              450000 guld\n    mizim:Income:guld                        -450000 guld\n    guld:Liabilities                         -450000 guld\n    guld:Equity:mizim                          450000 guld'.replace('mizim', name).replace('450000', amount))
            pf.close()
        if True:#not os.path.exists('/home/tigopay/ledger/guld/%s/included.dat' % name):
            pf = open('/home/tigopay/ledger/guld/%s/included.dat' % name, 'w')
            pf.write('include 1496275200.dat')
            pf.close()
        try:
            os.makedirs('/home/tigopay/people/%s' % name)
        except Exception:
            pass
        if not os.path.exists('/home/tigopay/people/%s/.gap.json' % name):
            pf = open('/home/tigopay/people/%s/.gap.json' % name, 'w')
            pf.write('{"path":"/people/%s","observer":"%s"}' % (name, name))
            pf.close()
        new.write('include %s/included.dat\n' % name)
new.close()
