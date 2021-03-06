from abc import abstractmethod, ABC

from domain import Frame


class Matcher(ABC):
    @abstractmethod
    def match(self, frame: Frame) -> float:
        pass


class ReferenceMatcher(Matcher):
    def __init__(self, reference_frame: Frame):
        self.reference_frame = reference_frame

    @abstractmethod
    def match_frame(self, frame: Frame) -> float:
        pass

    def match(self, frame: Frame) -> float:
        if self.reference_frame == frame:
            return 0
        return self.match_frame(frame)