hi = int(input()) * 60
mi = int(input())
hf = int(input()) * 60
mf = int(input())
ht = (hi + mi) - (hf + mf)
mt = ((hf + mf) - (hi + mi)) % 60
if ht < 0:
    ht = -1 * (ht / 60)
else:
    ht = (ht - 1440) // -60
ht = ht // 1
print(f"{ht:0>2.0f}:{mt:0>2.0f}")
