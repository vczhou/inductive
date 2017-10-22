var books = new Array("Genesis", "Exodus", "Leviticus", "Numbers", "Deuterononmy", "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
	"1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes",
	"Song of Solomon", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah",
	"Nahum", "Habbakuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "--------", "Matthew", "Mark", "Luke", "John", "Acts", "Romans",
	"1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
	"1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation")

// States
var chapters = new Array(0, 50, 40, 27, 36, 34, 24, 21, 4, 31, 24,
	22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12,
	8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7,
	3, 3, 3, 2, 14, 4, 0, 28, 16, 24, 21, 28, 16,
	16, 13, 6, 6, 4, 4, 5, 3,
	6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22)

function populateChapters( bookElementId, chapterElementId ){
	
	var selectedBookIndex = document.getElementById( bookElementId ).selectedIndex;

	var chapterElement = document.getElementById( chapterElementId );
	
	chapterElement.length=0;	// Fixed by Julian Woods
	chapterElement.options[0] = new Option('Chapter','');
	chapterElement.selectedIndex = 0;
	
	//var chapter_arr = _.range(1, chapters[selectedBookIndex] + 1);
	var chapter_arr = range(1, chapters[selectedBookIndex])
	for (var i=0; i<chapter_arr.length; i++) {
		chapterElement.options[chapterElement.length] = new Option(chapter_arr[i],chapter_arr[i]);
	}
}

function range(start, count) {
      return Array.apply(1, Array(count))
        .map(function (element, index) { 
          return index + start;  
      });
}

function getReference() {
	  var book=$('#book option:selected').html();
	  book = book.replace(' ', '_');
      var chapter=$('#chapter option:selected').html();
      url = "http://localhost:8000/" + book + "_" + chapter;
      window.location.replace(url);
}

function populateBooks(bookElementId, chapterElementId){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var bookElement = document.getElementById(bookElementId);
	bookElement.length=0;
	bookElement.options[0] = new Option('Book','-1');
	bookElement.selectedIndex = 0;
	for (var i=0; i<books.length; i++) {
		bookElement.options[bookElement.length] = new Option(books[i],books[i]);
	}

	// Assigned all countries. Now assign event listener for the states.

	if( chapterElementId ){
		bookElement.onchange = function(){
			populateChapters( bookElementId, chapterElementId );
		};
	}
}
