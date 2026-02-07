from libzim.reader import Archive
from libzim.search import Query, Searcher
from libzim.suggestion import SuggestionSearcher
from bs4 import BeautifulSoup

zim = Archive("E:/WikiFull/wikipedia_en_all_nopic_2025-12.zim")
print(f"Main entry is at {zim.main_entry.get_item().path}")
search_string = "Quantum"
suggestion_searcher = SuggestionSearcher(zim)
suggestion = suggestion_searcher.suggest(search_string)
suggestion_count = suggestion.getEstimatedMatches()
print(f"there are {suggestion_count} matches for {search_string}")
print(list(suggestion.getResults(0, suggestion_count)))

results = suggestion.getResults(0, suggestion_count)
for result in results:
    print(result)
    try:
        title = result.replace("_", " ")
        entry = zim.get_entry_by_title(title)
        print(entry)
        html = bytes(entry.get_item().content).decode("utf-8", errors="replace")
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
    except Exception as e:
        print(e)
    item = entry.get_item()
    # content = item.content.decode("utf-8", errors="replace")
    print(item)