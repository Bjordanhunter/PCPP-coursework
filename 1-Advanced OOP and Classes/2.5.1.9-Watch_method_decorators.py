class Watch:
    watchesCreated = 0
    
    def __init__(self):
        Watch.watchesCreated += 1
        self.engraving = ""

    @classmethod
    def get_num_of_watches(cls):
        return cls.watchesCreated

    @classmethod
    def engrave(cls, engravement):
        if cls.validate_engraving(engravement):
            watch = Watch()
            watch.engraving = engravement
            return watch

    @staticmethod
    def validate_engraving(text):
        if len(text) > 40 or not text.isalnum():
            raise typeError("invaild engravement: less then 40 chars and alphnums only")
        else:
            return True

Watch()
for e in ["foo@baz.com","valid","hello world","abc","123"]:
    try:
        Watch.engrave(e)
    except:
        print(f"{e} was not valid")

print(Watch.get_num_of_watches())
