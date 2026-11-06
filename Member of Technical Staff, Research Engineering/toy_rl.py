import random
N=5
ACTIONS=(-1,1)

def step(state, action):
    next_state=max(0,min(N-1,state+action))
    done=next_state==N-1
    reward=1.0 if done else -0.01
    return next_state,reward,done

def train(seed=42, episodes=500, alpha=.2, gamma=.95, epsilon=.2):
    rng=random.Random(seed)
    q={(s,a):0.0 for s in range(N) for a in ACTIONS}
    for _ in range(episodes):
        s=0
        for _ in range(20):
            a=rng.choice(ACTIONS) if rng.random()<epsilon else max(ACTIONS,key=lambda k:q[s,k])
            ns,r,done=step(s,a)
            target=r if done else r+gamma*max(q[ns,k] for k in ACTIONS)
            q[s,a]+=alpha*(target-q[s,a])
            s=ns
            if done:break
    return q

def evaluate(q):
    s=0
    history=[s]
    for t in range(20):
        a=max(ACTIONS,key=lambda k:q[s,k])
        s,r,done=step(s,a)
        history.append(s)
        if done:return {"success":True,"steps":t+1,"trace":history}
    return {"success":False,"steps":20,"trace":history}

if __name__=="__main__":
    print(evaluate(train()))
