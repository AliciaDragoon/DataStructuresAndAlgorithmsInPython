# 利用2.4.2节的ArithmeticProgression类，以0开始，增量为128，在达到整数2^63，或者更大的数时，我们需要执行多少次的调用。
from ch02.progressions import ArithmeticProgression
ap = ArithmeticProgression(128, 0)
count = 0
target = 2**63
while next(ap) < target:
    count += 1
print("需要调用次数:", count + 1)
# 2^56+1