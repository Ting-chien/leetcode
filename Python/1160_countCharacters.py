from operator import ne
from typing import List

class Solution1:
    '''
    Solition 1 comes with the idea of turning character in chars into
    a dictionary and counting if those characters can be consist to a
    word in words. If YES, those word will be saved in an array and return
    all the length of the words.
    '''
    def countCharacters(self, words: List[str], chars: str) -> int:

        d = {}
        # Build a dictionary with 24 slot
        for i in range(ord('a'), ord('z')+1):
            d[chr(i)] = None
        
        # Turn chars into a dictionary
        for char in chars:
            if not d[char]:
                d[char] = 1
            else:
                d[char] += 1

        # Check the words can be consist of chars
        result = 0
        for word in words:
            copy_d = d.copy()
            exist = True
            print(f'In word {word} the d is {copy_d}')
            for char in word:
                if not copy_d[char]:
                    exist = False
                    break
                else:
                    copy_d[char] -= 1
                    if copy_d[char] == 0:
                        copy_d[char] = None
            if exist:
                result += len(word)

        return result

class Solution2:
    '''
    This solution consist with two parts. First, you should sort the
    chars, and compare with a sorted string.
    '''
    def countCharacters(self, words: List[str], chars: str) -> int:

        # Prepare a sorted arr
        sorted_chars = sorted(chars)

        res = 0
        for word in words:
            sorted_word = sorted(word)
            j = 0
            # Iterate all sorted chars
            for i in range(len(sorted_chars)):
                if sorted_word[j] == sorted_chars[i]: j += 1
                if j == len(sorted_word):
                    res += j
                    break

        return res

class Solution3:
    '''
    Use a list(26 spaces) to store all chars and compare if the
    chars are enough for the word.
    '''
    def countCharacters(self, words: List[str], chars: str) -> int:

        res = 0

        # Prepare a available chars arr
        available = [0]*26
        for char in chars:
            index = ord(char) - 97
            available[index] += 1
        
        # Iterate all words
        for word in words:

            need = [0]*26
            for char in word:
                index = ord(char) - 97
                need[index] += 1

            isValid = True
            for i in range(26):
                if need[i] > available[i]:
                    isValid = False
                    break
            
            if isValid: res += len(word)

        return res



if __name__ == '__main__':
    sol = Solution3()
    ans1 = sol.countCharacters(["cat","bt","hat","tree"], "atach")
    print(f'ans1 = {ans1}')
    ans2 = sol.countCharacters(["hello","world","leetcode"], "welldonehoneyr")
    print(f'ans2 = {ans2}')
    ans3 = sol.countCharacters(["pxlqovnbsgvqjzpfeidchzrodnbqfrccfydzjptukscjuatlsrcurepllxzyghhdepitqptlmfkhzxjgswaulxkfydhkilg","uqklvqnlhdkwryjawkqfajfpbcnhglxlwxlaskxlytr","jvgkxcdkxrvfahjkvhmfuyjzxtyxrsogbtsjybeaxugqymcr","rgxditmosplnqvodtis","jm","ruqjwejuanjtiizcmbieobesnjnadzqvqumggblzmkxilgfarnxwpcawtkzxlvugibpidvwtikloeziuxqoi","wxeyzrnbhlhwxecrgejsrawyulynvgtszwqqlihkcvckgcgtgpyqtkuwvjywmhpskaiwmpyarftqhnogxpith","vdpbykqlihtpvfnqbrcjpggojqbalerohyitktuikbffvfatcnneuvbanjihiaorrjcdthntnrxebfhvshmpodmzhtwnasbm","wgjstkoaojcesfdrllugmojwdmgeejyiqvshlowtktddattunarnohgvqsoskfmbrami","ecwqxbawirvnxvsjybbebclaturorlcbpf","gtjbaigvufrotlwfoqqolnjabnvtbcygtfcytinzpcjbvprdkdjawrcbthmxjrabimhhs","cvzlbrvppkyxtjxzeglzwoagmpjnfxddbwolxmwdohgtfktgftzzkwpianslkpldyfzubtjczse","neaw","mxhmvkajofnmdiiduactlemcvpztscmsnrdhuhquxnnzywsrzxyplgbppiypxwcfbsnyzblaeifo","krekecabfpufucjhqphjnibaeqdvdpmrfougdwugvoioqangdnxromwlxnfeydaneyazzclscqgdxlhhgnoqmslfflzqv","klutvchxsceihfmzitgqakytesfjykribjhjzdruuoycjkwaghmmqkfrhkrtawudtjyjwqbyspamlegqjlwlj","raykfkflqdzrpthdejetwolgciygwaktulkxemkdbbllkjxhnnafsms","os","xhchkcetmlprcdmrnalvkvgabxxnomphqpqhnddqhecogspbdebeoshvjgzvmqu","jqtdysnpskktynxwmsfaabglagnqcllptvuyyqjwrmqaftenusmsahhhqubkwxltpr","sulmwluiwvlroldpiyecaicwrawzwflokefqkdwmxejaovvpbflfdtviinbvvtlhhhefmgfsqs","sxyhcckvyl","vsaacsybcddxvuzkddjmuivsvtjyanpbydmkcwnkmxvsiantgkvkmqjysclsvd","sxcghypulvmfqfunxj","pozekufhlooosxpcggbi","xzaoxzllcixfqbupqozmzrnugj","j","tgslwp","ntrdkixexajlpjgmcbrqimwtqnzfrqjszeiuvrgzclerzmsnagzaxbredvlrmipzflrzusclckmxphc","ifdflsywdfizpodsehrrifsvejcxarrxmxyjgbbvqyqvywncphzfmnxhybxpdcozfnzablfx","uluhplzrsaehaqxfnbcmixueedevhirbwqdyztwaxnkogcauymxgcpabxekib","agtfkinbdccoemxetbryzpluzlpyzicnfopphrxriqm","pdympxpwvxwcqaxrvbvyqkrresrjgzgxuyfxtkgldtathokdbyfsqfmitmiyagtqgijaiazvsumeyutbbwxqdshquzrehn","rqe","sljsvenhhstnnngzqyo","dezrzpgldeimxfoqajuhjctgvalwkhkjemjaxumxqmifglbizusuqlttxirpbqbuvauwy","dkwpyezbmkcskoxxcgrxcewknqgdckjxfyzcmzqcbyeucxbqybxoldogtkmdknsrruvnlfqnpfx","sjeftmjkuperfynbreycwhuoyqybticswblbrrpugzhlrmiedjqufnehevzqwtaebwvdswsz","lolnfyliloqmhjmhhohdtgfajjfdjqpubslbsrwitbjmrcegdrdjzvonxaefdvdfcbqmaaks","qhcoaiocjhuzywkirlblajgeapzajqsoa","sxrmoqxqbtakuqwmrrkljmegbwbeqbywmlyuprwyhljzejbybxoumidpxdrohwdjoqycpxcmivaulnqzneydwqfsvcxgyyseuk","yrowy","dohrzkrzdjehpctnjrvhzojullsiucrhphshwxwicyzkvzbqrztic","rmshnxtbhsdgkiijrmwulocdzjzpgfyimkjdthuzkhoqgkeawgwincubrloknocxwzgqqcxafksxgzh","aymovnuhptozhkiyowbeguzlkmrwjnujgjbdne","abc","vxoigovwmqizmkwbkktqk","uokwktdempzloaglvvkqstztmwzcmhgxtoua","bzwjxqueazlzfojrkbqmhtwrvuwsnfcnylurnddpektekca","qgndjgvzcyajhgmrrnhdywwdbmkhtthwcfiueuxfldanyrmccwcy"], "figspbov")
    print(f'ans3 = {ans3}')