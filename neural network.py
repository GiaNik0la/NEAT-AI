import random
import math

class info:
  def __init__(self, weight, info_itself):
    self.weight = weight
    self.info_itself = info_itself

def run(weightY, weightBottomY, weightUpY):
  PlayerY = 0
  WeightY = weightY

  BottomPipeY = -7
  WeightBottomY = weightBottomY

  UpPipeY = 1
  WeightUpY = weightUpY

  first_layer = [
    info(PlayerY, WeightY),
    info(BottomPipeY, WeightBottomY),
    info(UpPipeY, WeightUpY)
  ]

  weighted_sum = 0

  for i in range(len(first_layer)):
    multi = first_layer[i].weight * first_layer[i].info_itself
    weighted_sum += multi

  NeedJump = math.tanh(weighted_sum)

  return NeedJump

def Generations():
  generation = [
    run(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)),
    run(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)),
    run(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)),
    run(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)),
    run(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)),
    run(random.randint(-20, 20), random.randint (-20,20), random.randint(-20, 20)),
    run(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20))
  ]

  return generation

answer = -1

generation = Generations()

def fittness():
  for i in range(len(generation)):
    max = 0
    best = run(1, 1, 1)
    if generation[i] - answer <= max:
      max = generation[i] / answer
      best = generation[i]
    
  return best

def OtherGenerations():
  for i in range(len(generation)):
    generation[i] = fittness()

while fittness() != answer:
  OtherGenerations()

print(fittness())