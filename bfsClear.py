import numpy as np
import scipy.misc
import argparse
import sys
import os


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


class BFSClear:
    def __init__(self, image_shape=(2448, 2448), thres=64, verbose=1):
        self.seen = np.zeros(image_shape, dtype=np.bool)
        self.image_shape = image_shape
        self.verbose = verbose
        self.thres = thres

    def clear_image(self, image):

        self.seen = np.zeros(self.image_shape, dtype=np.bool)
        self.image = self.encode(image)
        for x in range(self.image_shape[0]):
            for y in range(self.image_shape[1]):
                if not self.seen[x, y]:
                    region = self.bfsSearch((x, y))
                    area = np.sum(region)
                    if area < self.thres:
                        copy_pos = (x - 1, y) if x > 0 else (x, y - 1)
                        if self.verbose:
                            print(
                                'Class: %2d  | Pos: ( %4d , %4d )  | Area: %4d pixel' % (self.image[x, y], x, y, area))
                        if x > 0:
                            self.image[region] = self.image[x - 1, y]
                        elif y > 0:
                            self.image[region] = self.image[x, y - 1]
                    self.seen = self.seen + region

        return self.decode(self.image)

    def bfsSearch(self, pos):

        frontier = Queue()
        frontier.push(pos)
        region = np.zeros(self.image_shape, dtype=np.bool)
        region[pos] = True
        target = self.image[pos]

        while True:
            if frontier.isEmpty():
                return region
            else:
                node = frontier.pop()

            '''
            if problem.isGoalState(node):
                path = []
                startState = problem.getStartState()
                while node != startState:
                    path.append(transitionTable[node][1])
                    node = transitionTable[node][0]
                path.reverse()
                return path
            '''
            x = node[0]
            y = node[1]
            successors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for next_pos in successors:
                if 0 <= next_pos[0] < self.image_shape[0] and 0 <= next_pos[1] < self.image_shape[1]:
                    if not region[next_pos] and self.image[next_pos] == target:
                        frontier.push(next_pos)
                        region[next_pos] = True

    def encode(self, image):

        image = (image >= 128).astype(np.uint8)
        image = 4 * image[:, :, 0] + 2 * image[:, :, 1] + image[:, :, 2]
        cat_image = np.zeros(self.image_shape, dtype=np.uint8)
        cat_image[image == 3] = 0  # (Cyan: 011) Urban land
        cat_image[image == 6] = 1  # (Yellow: 110) Agriculture land
        cat_image[image == 5] = 2  # (Purple: 101) Rangeland
        cat_image[image == 2] = 3  # (Green: 010) Forest land
        cat_image[image == 1] = 4  # (Blue: 001) Water
        cat_image[image == 7] = 5  # (White: 111) Barren land
        cat_image[image == 0] = 6  # (Black: 000) Unknown

        return cat_image

    def decode(self, cat_image):

        image = np.zeros((*self.image_shape, 3), dtype=np.uint8)
        image[cat_image == 0] = [0, 255, 255]
        image[cat_image == 1] = [255, 255, 0]
        image[cat_image == 2] = [255, 0, 255]
        image[cat_image == 3] = [0, 255, 0]
        image[cat_image == 4] = [0, 0, 255]
        image[cat_image == 5] = [255, 255, 255]
        image[cat_image == 6] = [0, 0, 0]

        return image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', help='input image directory', type=str)
    parser.add_argument('-o', '--output', help='output image directory', type=str)
    args = parser.parse_args()

    clearer = BFSClear(thres=2000, verbose=0, image_shape=(1224, 1224))

    file_list = [file for file in os.listdir(args.image) if file.endswith('.png')]
    for i, file in enumerate(file_list):
        sys.stdout.write('\rProgress: %3d / %3d    %s' % (i, len(file_list), file))
        sys.stdout.flush()
        image = scipy.misc.imread(os.path.join(args.image, file))
        image = scipy.misc.imresize(image, (1224, 1224), interp='nearest')
        cleared_image = clearer.clear_image(image)
        cleared_image = scipy.misc.imresize(cleared_image, (2448, 2448), interp='nearest')
        scipy.misc.imsave(os.path.join(args.output, file), cleared_image)
