class FindLiars:

    def __init__(self):
        self.number_of_tests = int(input())
        self.option_map = {"L": 0, "T": 1}
        self.test_matrices = []
        self.setup_inputs()
        self.find_liars()

    def setup_inputs(self):
        for i in range(self.number_of_tests):
            student_matrix = []
            number_of_students = int(input())
            for i in range(number_of_students):
                student_response = [self.option_map[i] for i in input()]
                student_matrix.append(student_response)
            self.test_matrices.append(student_matrix)
    
    def find_liars(self):
        for i, matrix in enumerate(self.test_matrices):

            atleast, atmost = self.get_liars(matrix)
            if atleast > atmost or ((atleast == atmost == len(matrix))):
                print("Class Room#{} is paradoxical".format(i+1))
            else:
                print("Class Room#{} contains atleast {} and atmost {} liars".format(i+1, atleast, atmost))

    def get_liars(self, matrix):
        definite_liars = set()
        possible_truths = set()
        size = len(matrix)
        atleast = 0
        for i in range(size):
            if matrix[i][i] == 0:
                definite_liars.add(i)
            else:
                possible_truths.add(i)

        truth_friends = {}
    
        for i in possible_truths:
            truth_friends[i] = {index for index, value in enumerate(matrix[i]) if value ==1}

        for index, value in truth_friends.items():
            if value.intersection(definite_liars): 
                possible_truths.remove(index)
                definite_liars.add(index)

        for index, value in truth_friends.items():

            if value.intersection(definite_liars): 
                possible_truths.discard(index)
                definite_liars.add(index)
                continue

            for elem in value:
                if truth_friends[elem] != value:
                    definite_liars.add(index)
                    possible_truths.discard(index)
                    break

        vals = []
        set_of_truth_vals = []
        total = 0
        for elem in possible_truths:
            if truth_friends[elem] not in set_of_truth_vals:
                set_of_truth_vals.append(truth_friends[elem])
        # print(set_of_truth_vals)

        for elem in set_of_truth_vals:
            vals.append(len(elem))
        
        total = sum(vals)
        min_vals = [total - i for i in vals]
        liar_count = len(definite_liars)

        if len(min_vals) > 1:
            liar_count+= min(min_vals)
        # print(matrix)
        atmost = len(matrix)
        # print(atmost)
        # print(liar_count)
        # print(definite_liars)
        for liar in definite_liars:
            if sum(matrix[liar]) == len(matrix):
                # print("here")
                atmost = atmost -1
                break

        return liar_count, atmost


def main():
    FindLiars()

if __name__ == '__main__':
  main()