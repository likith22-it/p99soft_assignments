from members.member import Member


class Faculty(Member):

    def __init__(self,
                 member_id,
                 name):

        super().__init__(
            member_id,
            name
        )

        self._max_limit = 5