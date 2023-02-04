# /usr/local/bin/env python3


# Translate Python applications using Qt .ts files without the need for compilation

import os
import locale

try:
    # sudo python3 -m pip install translate-toolkit
    from translate.storage.ts2 import tsfile
except:
    print("The Python module 'translate' is not available. The application will run untranslated.")


class TsTranslator(object):

    def __init__(self, translations_dir, translations_file_prefix):
        self.ts = None
        long_locale = locale.getlocale()[0]  # de_DE
        short_locale = long_locale.split("_")[0]  # de
        candidates = [long_locale, short_locale, "en", "en_US"]
        for candidate in candidates:
            p = translations_dir + "/" + candidate + ".ts"
            if translations_file_prefix:
                p = translations_dir + "/" + translations_file_prefix + "_" + candidate + ".ts"
            if os.path.exists(p):
                # print(p)
                try:
                    self.ts = tsfile.parsefile(p)
                    print("Loaded translations from %s" % p)
                    break
                except:
                    print("Translations could not be loaded.")
                    break
        if not self.ts:
            print("Could not find suitable .ts files in %s" % translations_dir)

    def tr(self, input):
        if not self.ts:
            return (input)
        unit = self.ts.findunit(input)
        if not unit:
            return (input)
        output = unit.target
        if not output:
            return (input)
        return (output)


if __name__ == "__main__":
    tstr = TsTranslator(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))) + "/i18n", None)
    print(tstr.tr("Hello World"))
