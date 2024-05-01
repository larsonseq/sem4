def FIFO(incoming_stream, frames, pages):
    page_faults = 0
    temp = [-1] * frames
    frame_list = [[] for _ in range(frames)]
    lastr = 0
    for page in incoming_stream:
        if page not in temp:
            page_faults += 1
            if -1 in temp:
                temp[temp.index(-1)] = page
            else:
                temp[lastr] = page
                lastr += 1
                if lastr >= frames:
                    lastr = 0

        for i, frame in enumerate(frame_list): 
            if temp[i] != -1:
                frame.append(temp[i])
            else:
                frame.append("-")

    print("Total Page Faults: ", page_faults)
    print("Frames:")
    for i, frame in enumerate(frame_list, 1):
        print(f"Frame {i}: {' '.join(str(page) for page in frame)}")


def optimal(incoming_stream, frames, pages):
    page_faults = 0
    temp = [-1] * frames
    frame_list = [[] for _ in range(frames)]

    for idx, page in enumerate(incoming_stream):
        if page not in temp:
            page_faults += 1
            if -1 in temp:
                temp[temp.index(-1)] = page
            else:
                max_future_idx = max((incoming_stream[idx:].index(p) if p in incoming_stream[idx:] else float('inf'), i) for i, p in enumerate(temp))[1]
                temp[max_future_idx] = page

        for i, frame in enumerate(frame_list):
            if temp[i] != -1:
                frame.append(temp[i])
            else:
                frame.append("-")

    print("Total Page Faults: ", page_faults)
    print("Frames:")
    for i, frame in enumerate(frame_list, 1):
        print(f"Frame {i}: {' '.join(str(page) for page in frame)}")


def lru(incoming_stream, frames, pages):
    page_faults = 0
    temp = [-1] * frames
    frame_list = [[] for _ in range(frames)]
    recent_dict = {}

    for idx, page in enumerate(incoming_stream):
        if page not in temp:
            page_faults += 1
            if -1 in temp:
                temp[temp.index(-1)] = page
                recent_dict[page] = idx
            else:
                least_recent_page = min(recent_dict, key=recent_dict.get)
                replace_idx = temp.index(least_recent_page)
                temp[replace_idx] = page
                recent_dict.pop(least_recent_page)
                recent_dict[page] = idx
        else:
            recent_dict[page] = idx

        for i, frame in enumerate(frame_list):
            if temp[i] != -1:
                frame.append(temp[i])
            else:
                frame.append("-")

    print("Total Page Faults: ", page_faults)
    print("Frames:")
    for i, frame in enumerate(frame_list, 1):
        print(f"Frame {i}: {' '.join(str(page) for page in frame)}")


def main():
    incoming_stream = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]  
    frames = 3 #int(input("Enter the number of frames: "))
    pages = 20 #int(input("Enter the number of pages: "))
    print("Enter the page reference string: ")
    # for i in range(pages):
    #     incoming_stream.append(int(input()))


    # Call FIFO algorithm
    print("\nFIFO Algorithm:\n")
    FIFO(incoming_stream, frames, pages)


    # Call Optimal algorithm
    print("\nOptimal Algorithm:\n")
    optimal(incoming_stream, frames, pages)


    # Call LRU algorithm
    print("\nLRU Algorithm:\n")
    lru(incoming_stream, frames, pages)

if __name__ == "__main__":
    main()

