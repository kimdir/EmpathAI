import nltk

class NLProcessor:
    def __init__(self):
        self.sampleText = ""
        self.textSentiment = 0.0
        self.evalFlag = False
        self.stopwords = nltk.corpus.stopwords.words("english")

    def LoadSample(self,inputSample):
        """Method to isolate sample loading for config."""

        self.sampleText = inputSample

    def Output(self):
        """Method to isolate output for config."""
        return [self.textSentiment,self.evalFlag]

    def AnalyzeSample(self):
        """Primary method for analyzing text samples."""

    def TokenizeToWords(self):
        """Method for tokenizing samples to words."""
        # Tokenize the sample
        textTokens = nltk.word_tokenize(self.sampleText)
        if debug:
            print("Tokenizing Step")
            print(self.sampleText)
            print(textTokens)

        # Normalize the tokens
        textTokens = [token.lower() for token in textTokens if token.isalpha()]
        textTokens = [token for token in textTokens if token not in self.stopwords]
        if debug:
            print("Normalizing Step")
            print(self.sampleText)
            print(textTokens)

        return textTokens

        def TokenizeSentences(self):
            """Method for tokenizing sentences. Isolated for customization"""
            textTokens =

if __name__ == ("__main__"):
    debug = True
    text = "Debugging the program, and this is the debug text. Check 1, Check 2, Check 3"
    print(text)
    NLProcessor = NLProcessor()
    NLProcessor.LoadSample(text)
    NLProcessor.AnalyzeSample()
