import hashlib


def main():

    algorithms_set = hashlib.algorithms_available
    algorithms_set = list(algorithms_set)
    algorithms_set.remove("shake_256")
    algorithms_set.remove("shake_128")

    x = str(input("x = "))
    r = str(input("r = "))

    data = r + ":" + x
    data = data.encode("utf-8")

    for algorithm in algorithms_set:

        hash_object = hashlib.new(algorithm, data)
        hash_value = hash_object.hexdigest()
        print(f"{algorithm} : {hash_value} \n")


if __name__ == "__main__":
    main()
