import datetime

class Logger:
    COLORS = {
        'reset': "\033[0m",
        'cyan': "\033[1;36m",
        'blue': "\033[1;34m",
        'purple': "\033[1;35m",
        'yellow': "\033[1;33m",
        'green': "\033[1;32m",
        'red': "\033[1;31m",
    }

    @staticmethod
    def _timestamp():
        return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    @classmethod
    def info(cls, msg, color='cyan'):
        print(f"{cls._timestamp()} {cls.COLORS[color]}{msg}{cls.COLORS['reset']}")

    @classmethod
    def user_input(cls, msg):
        print(f"\n{cls.COLORS['blue']}You:{cls.COLORS['reset']} {msg}")

    @classmethod
    def request(cls, msg):
        print(f"{cls._timestamp()} {cls.COLORS['purple']}[REQUEST]{cls.COLORS['reset']} {msg}")

    @classmethod
    def thinking(cls, msg="Processing request..."):
        print(f"{cls._timestamp()} {cls.COLORS['yellow']}[THINKING]{cls.COLORS['reset']} {msg}")

    @classmethod
    def response(cls, msg):
        print(f"\n{cls.COLORS['green']}Assistant:{cls.COLORS['reset']} {msg}")

    @classmethod
    def warn(cls, msg):
        print(f"{cls._timestamp()} {cls.COLORS['yellow']}{msg}{cls.COLORS['reset']}")

    @classmethod
    def error(cls, msg):
        print(f"{cls._timestamp()} {cls.COLORS['red']}[ERROR]{cls.COLORS['reset']} {msg}")

    @classmethod
    def interrupt(cls, msg="Interrupt detected, exiting safely..."):
        print(f"{cls._timestamp()} {cls.COLORS['red']}[INTERRUPT]{cls.COLORS['reset']} {msg}")

    @classmethod
    def agent_start(cls, agent_name):
        print(f"{cls._timestamp()} {cls.COLORS['cyan']}[AGENT START]{cls.COLORS['reset']} Agent started: {agent_name}")

    @classmethod
    def tool_call(cls, tool_name):
        print(f"{cls._timestamp()} {cls.COLORS['yellow']}[TOOL CALL]{cls.COLORS['reset']} Tool called: {tool_name}")

    @classmethod
    def tool_result(cls, tool_name, result):
        print(f"{cls._timestamp()} {cls.COLORS['green']}[TOOL RESULT]{cls.COLORS['reset']} {tool_name} => {result}...")

    @classmethod
    def handoff(cls, from_agent, to_agent):
        print(f"{cls._timestamp()} {cls.COLORS['purple']}[HANDOFF]{cls.COLORS['reset']} {from_agent} → {to_agent}")