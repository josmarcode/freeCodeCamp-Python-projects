import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for k, v in balls.items():       # Fill hat
            for i in range(v):
                self.contents.append(k)

    def __str__(self):
        return str(self.contents)

    def draw(self, n):
        # print("Class content=", self.contents)
        if n < len(self.contents):
            inds = sorted(random.sample(range(len(self.contents)),
                          n), reverse=True)    # n random index
            out = []
            for i in range(n):
                # Out list is filled with random elements of hat
                out.append(self.contents[inds[i]])
                # These random elements are deleted from hat
                del self.contents[inds[i]]
            # print('Class:', out)
            return out

        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Counter controller and successful counter
    count, success = 0, 0
    # print(hat)
    while count < num_experiments:
        fail = 0
        # Copy of hat is created
        copy_hat = copy.deepcopy(hat)
        # print(f'Copia: {copy_hat} \n Original: {hat}')
        # Draw with copy of hat
        draw = copy_hat.draw(num_balls_drawn)
        # print(f'iter={count} - {draw}\n\n')
        for k, v in expected_balls.items():
            # Verifying that draw contain extpected balls
            if draw.count(k) >= v:
                pass
            else:
                fail += 1                                                   # if not, fail exist
                # print('Falló')
        if not fail:
            # if not fail, successful
            success += 1
            print(f'Éxito. Iteration={count} (Fail: {fail})')
            print(f'Draw={draw}\n')
        count += 1

    return success / num_experiments
