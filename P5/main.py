from prob_calculator import Hat, experiment

sombrero_1 = Hat(rosa=2, morado=5, gris=1)

print(sombrero_1.draw(2))


probability = experiment(hat=sombrero_1, expected_balls={
                         "rosa": 2}, num_balls_drawn=2, num_experiments=500)

print(probability)
