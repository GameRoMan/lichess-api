import json


class Decoder(json.JSONDecoder):
    def decode(self, s, *args, **kwargs):
        lines = ",".join(s.splitlines())
        text = "[{}]".format(lines)
        return super(Decoder, self).decode(text, *args, **kwargs)


class Encoder(json.JSONEncoder):
    def encode(self, obj, *args, **kwargs):
        lines: list[str] = []
        for each in obj:
            line = super(Encoder, self).encode(each, *args, **kwargs)
            lines.append(line)
        return "\n".join(lines)
