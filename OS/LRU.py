from sys import maxsize
from mem_pretty_print import pp

# Implement LRU for frame replacement
def lru(requests, nr_frames):
    """
    LRU algorithm for frame replacement. Takes a list of page numbers we want to access and the number of frames.
    Returns a 2d histogram of the pages that are in each frame for each request.
    """
    # Contens of the frames
    frames = [-1] * nr_frames
    # Age of the frames
    ages = [maxsize] * nr_frames
    # Initialize the histogram
    frame_histogram = []
    age_histogram = []
    # Iterate over the requests
    for request in requests:
        if request in frames:
            # If the request is already in the frames, update the age of the frame
            for i in range(len(ages)):
                if ages[i] == maxsize:
                    continue
                ages[i] += 1 
            ages[frames.index(request)] = 0
        else:
            # If the request is not in the frames, find the oldest frame and replace it
            oldest_frame = ages.index(max(ages))
            frames[oldest_frame] = request
            for i in range(len(ages)):
                if ages[i] == maxsize:
                    continue
                ages[i] += 1
            ages[oldest_frame] = 0
        frame_histogram.append(frames.copy())
        age_histogram.append(ages.copy())
    return frame_histogram, age_histogram

def from_rlu(rlu):
    """
    Rotates the rlu histogram.
    """
    return [[rlu[j][i] for j in range(len(rlu))] for i in range(len(rlu[0]))]

if __name__ == "__main__":
    f = [int(x) for x in input("Enter the page requests (space separated): ").split()]
    c = int(input("Enter the page capacity: "))
    frames, ages = lru(f, c)
    print("Frames:")
    pp(from_rlu(frames))
    print("Ages:")
    pp(from_rlu(ages))
    input("Press enter to continue...")