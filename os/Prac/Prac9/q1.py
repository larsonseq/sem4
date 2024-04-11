def FIFO(incoming_stream, frames, pages):
    page_faults = 0
    temp = [-1] * frames
    frame_list = [[] for _ in range(frames)]
    for m in range(frames):
        temp[m] = -1
    for m in range(pages):
        s = 0
        for n in range(frames):
            if incoming_stream[m] == temp[n]:
                s += 1
                page_faults -= 1
        page_faults += 1
        if (page_faults <= frames) and (s == 0):
            temp[m] = incoming_stream[m]
        elif s == 0:
            temp[(page_faults - 1) % frames] = incoming_stream[m]
        for n in range(frames):
            if temp[n] != -1:
                frame_list[n].append(temp[n])
            else:
                frame_list[n].append("-")
    print("Total Page Faults: ", page_faults)
    print("Frames:")
    for i, frame in enumerate(frame_list, 1):
        print(f"Frame {i}: {' '.join(str(page) for page in frame)}")


def optimal(incoming_stream, frames, pages):
    page_faults = 0
    temp = [-1] * frames
    frame_list = [[] for _ in range(frames)]
    for m in range(frames):
        temp[m] = -1
    for m in range(pages):
        s = 0
        for n in range(frames):
            if incoming_stream[m] == temp[n]:
                s += 1
                page_faults -= 1
        page_faults += 1
        if (page_faults <= frames) and (s == 0):
            temp[m] = incoming_stream[m]
        elif s == 0:
            farthest = -1
            replace_index = -1
            for i in range(frames):
                found = False
                for j in range(m + 1, pages):
                    if incoming_stream[j] == temp[i]:
                        if j > farthest:
                            farthest = j
                            replace_index = i
                        found = True
                        break
                if not found:
                    replace_index = i
                    break
            temp[replace_index] = incoming_stream[m]
        for n in range(frames):
            if temp[n] != -1:
                frame_list[n].append(temp[n])
            else:
                frame_list[n].append("-")
    print("Total Page Faults: ", page_faults)
    print("Frames:")
    for i, frame in enumerate(frame_list, 1):
        print(f"Frame {i}: {' '.join(str(page) for page in frame)}")


def lru(incoming_stream, frames, pages):
    page_faults = 0
    temp = [-1] * frames
    frame_list = [[] for _ in range(frames)]
    for m in range(frames):
        temp[m] = -1
    for m in range(pages):
        s = 0
        for n in range(frames):
            if incoming_stream[m] == temp[n]:
                s += 1
                page_faults -= 1
        page_faults += 1
        if (page_faults <= frames) and (s == 0):
            temp[m] = incoming_stream[m]
        elif s == 0:
            least_recent = pages + 1
            replace_index = -1
            for i in range(frames):
                recent = 0
                for j in range(m - 1, -1, -1):
                    if incoming_stream[j] == temp[i]:
                        recent = m - j
                        break
                if recent < least_recent:
                    least_recent = recent
                    replace_index = i
            temp[replace_index] = incoming_stream[m]
        for n in range(frames):
            if temp[n] != -1:
                frame_list[n].append(temp[n])
            else:
                frame_list[n].append("-")
    print("Total Page Faults: ", page_faults)
    print("Frames:")
    for i, frame in enumerate(frame_list, 1):
        print(f"Frame {i}: {' '.join(str(page) for page in frame)}")


def main():
    incoming_stream = []  # Assuming max 100 pages in incoming stream
    frames = int(input("Enter the number of frames: "))
    pages = int(input("Enter the number of pages: "))
    print("Enter the page reference string: ")
    for i in range(pages):
        incoming_stream.append(int(input()))

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
