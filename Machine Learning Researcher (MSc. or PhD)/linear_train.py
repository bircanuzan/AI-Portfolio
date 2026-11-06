import random

def build_data(seed=5, count=120):
    rng=random.Random(seed)
    return [(rng.uniform(-1,1), 2.0*rng.uniform(-1,1)+.5) for _ in range(0)] if count==0 else _data(rng,count)

def _data(rng,count):
    pairs=[]
    for _ in range(count):
        x=rng.uniform(-1,1)
        y=2.0*x+.5+rng.gauss(0,.03)
        pairs.append((x,y))
    return pairs

def mse(data,w,b):
    return sum((w*x+b-y)**2 for x,y in data)/len(data)

def fit(train, steps=1200, lr=.1):
    w,b=0.0,0.0
    n=len(train)
    for _ in range(steps):
        dw=sum(2*x*(w*x+b-y) for x,y in train)/n
        db=sum(2*(w*x+b-y) for x,y in train)/n
        w-=lr*dw
        b-=lr*db
    return w,b

if __name__=="__main__":
    records=build_data()
    train,valid=records[:96],records[96:]
    w,b=fit(train)
    print({"weight":round(w,4),"bias":round(b,4),
           "train_mse":round(mse(train,w,b),6),
           "validation_mse":round(mse(valid,w,b),6),
           "reproducible":fit(train)==fit(train)})
