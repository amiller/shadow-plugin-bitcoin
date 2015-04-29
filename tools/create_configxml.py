import random

template = """
    <node id="{node}">
        <application plugin="bitcoind" time="13" arguments="-datadir=data/{node} -dbcache=4 -debug -printtoconsole {connect} -listen -par=2 -server=0 -rpcpassword=4J7YUKgRHd8hUWp14e233pwmkPtbnQ2cUS4PMxiy1J6z -checkblocks=1 -disablewallet=1"/>
    </node>
"""

def entries(n=10, n_conns=3):
    s = ''
    names = ['bcdnode%d'%i for i in range(1,n+1)]
    for i in range(n):
        rest = set(names)
        rest.remove(names[i])
        rest = list(rest)
        random.shuffle(rest)
        conns = ' '.join('-connect=%s'%c for c in rest[:n_conns])
        s += template.format(node=names[i], connect=conns)
    print s
