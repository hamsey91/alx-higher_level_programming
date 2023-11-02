#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Print all hidden name from directory
    for name in dir(hidden_4):
        if name[:2] != "__":
            print("{}".format(name))
