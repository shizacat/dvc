class Params(object):
    def __init__(self, repo):
        self.repo = repo

    def show(self, *args, **kwargs):
        from .show import show

        return show(self.repo, *args, **kwargs)

    def diff(self, *args, **kwargs):
        from .diff import diff

        return diff(self.repo, *args, **kwargs)
