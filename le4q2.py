try:
    import mylists
    import sys
except ImportError:
    print("ImportError exception: unable to locate the module")
else:
    try:
        f = open("lists.txt", 'r')
    except IOError:
        print("IOError exception: unable to locate the file")
    else:
        lst = []
        for i in f:
            lst.append(i.strip("\\n"))
        tmp = []
        for i in lst:
            tmp.append(list(map(float, i.split(','))))
        try:
            key_lst = (list(map(float, input().split(','))))
        except EOFError:
            print("EOFError exception: End of file reached")
            print("Invalid Key")

        except KeyboardInterrupt:
            print("KeyboardInterrupt exception: Interrupted by the keyboard")
            print("Invalid Key")

        except ValueError:
            print("ValueError exception: The input values are neither float not integer values")
            print("Invalid Key")
        else:
            print("Mean List is", end=" ")
            print()
            if len(key_lst) != len(tmp[0]):
                print("Invalid Key")
                sys.exit(0)
            k = mylists.mean_list(tmp)
            for i in k:
                print(i, end=" ")
            print("Distance between key_list and mean_list is", mylists.distance(k, key_lst))
            if mylists.is_in_set(k, tmp):
                print("mean_list is present in the provided set of lists")
            else:
                print("mean_list is not present in the provided set of lists")
            clo = mylists.closest_farthest(tmp, key_lst, False)
            far = mylists.closest_farthest(tmp, key_lst, True)
            print("the closest list is", end=" ")
            for i in clo:
                print(i, end=" ")
            print()
            print("the farthest list is", end=" ")
            for j in far:
                print(j, end=" ")
            print()
            print("The  distance between the closest list and the farthest list", end=" ")
            print(mylists.distance(clo, far))
