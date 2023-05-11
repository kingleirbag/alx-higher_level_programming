#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    hidden_dirs = = dir(hidden_4)
    for hidden_dir in hidden_dirs:
        if hidden_dir[:2] != "__":
            print(hidden_dir)
