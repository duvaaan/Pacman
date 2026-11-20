
import commentjson


YELLOW = "\033[93m"
RESET = "\033[0m"

DEFAULT_CONFIG = {
    "highscore_filename": "highscore.json",
    "levels": 3,
    "width": 15,
    "height": 15,
    "lives": 3,
    "pacgum": 66,
    "points_per_pacgum": 10,
    "points_per_super_pacgum": 50,
    "points_per_ghost": 200,
    "seed": 42,
    "level_max_time": 90
}


def config_parser(filename):
    try:
        with open(filename, "r") as file:
            config = commentjson.load(file)

        if not isinstance(config, dict):
            raise ValueError("CONFIG MUST BE A JSON OBJECT")

        # Ignore unknown keys
        config = {key: value for key, value in config.items()
                  if key in DEFAULT_CONFIG}

        # Add missing keys
        for key, value in DEFAULT_CONFIG.items():
            if key not in config:
                config[key] = value

        if type(config.get('levels')) != int or config.get('levels') < 1:
            config["levels"] = DEFAULT_CONFIG["levels"]
            print(f"{YELLOW}[WARNING] INVALID 'levels' VALUE, USING DEFAULT.{RESET}")

        if type(config.get('lives')) != int or config.get('lives') < 1:
            config["lives"] = DEFAULT_CONFIG["lives"]
            print(f"{YELLOW}[WARNING] INVALID 'lives' VALUE, USING DEFAULT.{RESET}")

        for i in ["points_per_ghost", "points_per_pacgum",
                  "points_per_super_pacgum"]:
            if type(config.get(i)) != int or config.get(i) < 1:
                config[i] = DEFAULT_CONFIG[i]
                print(f"{YELLOW}[WARNING] INVALID '{i}' VALUE, USING DEFAULT.{RESET}")

        for i in ["width", "height"]:
            if type(config.get(i)) != int or config.get(i) < 4:
                config[i] = DEFAULT_CONFIG[i]
                print(f"{YELLOW}[WARNING] INVALID '{i}' VALUE, USING DEFAULT.{RESET}")

        if type(config.get('level_max_time')) != int or config.get('level_max_time') < 10:
            config['level_max_time'] = DEFAULT_CONFIG["level_max_time"]
            print(f"{YELLOW}[WARNING] INVALID 'level_max_time' VALUE, USING DEFAULT.{RESET}")

        if type(config.get('seed')) != int or config.get('seed') < 0:
            config['seed'] = DEFAULT_CONFIG["seed"]
            print(f"{YELLOW}[WARNING] INVALID 'seed' VALUE, USING DEFAULT.{RESET}")

        if type(config.get('pacgum')) != int or config.get('pacgum') < 1:
            config['pacgum'] = DEFAULT_CONFIG["pacgum"]
            print(f"{YELLOW}[WARNING] INVALID 'pacgum' VALUE, USING DEFAULT.{RESET}")

        if (not isinstance(config.get('highscore_filename'), str)
                or not config.get('highscore_filename').strip()):
            config["highscore_filename"] = DEFAULT_CONFIG["highscore_filename"]
            print(f"{YELLOW}[WARNING] INVALID 'highscore_filename', USING DEFAULT.{RESET}")

        # Create highscore file without overwriting existing data
        try:
            with open(config["highscore_filename"].strip(), "a"):
                pass
        except OSError:
            print(f"{YELLOW}[WARNING] CANNOT OPEN HIGHSCORE FILE, USING DEFAULT.{RESET}")
            config["highscore_filename"] = DEFAULT_CONFIG["highscore_filename"]

        return config

    except (commentjson.JSONLibraryException, OSError, ValueError):
        print(f"{YELLOW}[WARNING] CONFIG FILE ERROR, USING DEFAULT VALUES.{RESET}")
        return DEFAULT_CONFIG

