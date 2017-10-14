from define import KEYMAP


class HiraganaToKatakana(object):
    def __init__(self):
        hiragana = (
            "あいうえお"
            "かきくけこ"
            "さしすせそ"
            "たちつてと"
            "なにぬねの"
            "はひふへほ"
            "まみむめも"
            "やゐゆゑよ"
            "らりるれろ"
            "わをん"
            "がぎぐげご"
            "ざじずぜぞ"
            "だぢづでど"
            "ばびぶべぼ"
            "ぱぴぷぺぽ"
            "ぁぃぅぇぉ"
            "ゃゅょっ"
        )
    
        katakana = (
            "アイウエオ"
            "カキクケコ"
            "サシスセソ"
            "タチツテト"
            "ナニヌネノ"
            "ハヒフヘホ"
            "マミムメモ"
            "ヤヰユヱヨ"
            "ラリルレロ"
            "ワヲン"
            "ガギグゲゴ"
            "ザジズゼゾ"
            "ダヂヅデド"
            "バビブベボ"
            "パピプペポ"
            "ァィゥェォ"
            "ャュョッ"
        )

        self.table = dict()
        for h, k in zip(hiragana, katakana):
            self.table[h] = k
    
    def __call__(self, hiragana):
        return self.table.get(hiragana)


def main():
    hiragana_to_katakana = HiraganaToKatakana()

    for first, seconds, chars in KEYMAP:
        assert len(seconds) == len(chars)
        for second, hiragana in zip(seconds, chars):
            keybind = first + second
            katakana = hiragana_to_katakana(hiragana)
            if katakana is None:
                continue
            print("{0},{1},{2},{2}".format(keybind, hiragana, katakana))

if __name__ == '__main__':
    main()
