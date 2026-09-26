class range:
    def __init__(self, *args):
        l = len(args)
        if l > 3:
            raise TypeError(f'range expected at most 3 arguments, got {l}')
        elif l == 0:
            raise TypeError('range expected at least 1 argument, got 0')

        for i in args:
            if not isinstance(i, int):
                raise TypeError(f'{type(i)} object cannot be interpreted as an integer')

        if l == 3:
            start, stop, step = args
            if step == 0:
                raise ValueError('range() arg 3 must not be zero')
        elif l == 2:
            (start, stop), step = args, 1
        else:
            start, stop, step = 0, *args, 1
        self.__start = start
        self.__index = -1
        self.__stop = stop
        self.__step = step

    def __len__(self):
        return max(0, (self.stop - self.start) // self.step + bool((self.stop - self.start) % self.step))

    def __getitem__(self, item):
        if item >= len(self) or item <= -len(self) - 1:
            raise IndexError('range object index out of range')
        if item < 0:
            item = len(self) + item
        return self.start + self.step * item

    def __next__(self):
        self.__index += 1
        if (
                (self.step > 0 and self.start + self.step * self.__index >= self.stop)
                or (self.step < 0 and self.start + self.step * self.__index <= self.stop)
        ):
            self.__index = -1
            raise StopIteration
        return self.start + self.step * self.__index

    def __iter__(self):
        return self

    def __repr__(self):
        return f'range({self.__start}, {self.__stop})' if self.__step == 1 else f'range({self.__start}, {self.__stop}, {self.__step})'

    def index(self, value):
        if (
                (self.step > 0 and (value >= self.stop or value < self.start))
                or (self.step < 0 and (value <= self.stop or value > self.start))
        ):
            raise ValueError(f'{value} is not in range')
        elif value % int(value):
            raise ValueError('sequence.index(x): x not in sequence')

        res = (value - self.start) / self.step

        if res and res % int(res) != 0:
            raise ValueError(f'{value} is not in range')
        return int(res)

    @property
    def start(self):
        return self.__start

    @property
    def stop(self):
        return self.__stop

    @property
    def step(self):
        return self.__step

    @start.setter
    def start(self, value):
        raise AttributeError('readonly attribute')

    @stop.setter
    def stop(self, value):
        raise AttributeError('readonly attribute')

    @stop.setter
    def stop(self, value):
        raise AttributeError('readonly attribute')

if __name__ == '__main__':
    r = range(11)
    print(sum(r))
