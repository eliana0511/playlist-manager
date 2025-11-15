# 🎵 Playlist Manager
# Author: A.B.
# Description: Demonstrates a linked list by managing songs in a playlist.

class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None  # pointer to next song

class Playlist:
    def __init__(self):
        self.head = None  # first song in playlist

    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
            print(f"🎶 Added '{title}' as the first song in the playlist.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_song
        print(f"🎶 Added '{title}' to the playlist.")

    def display(self):
        if not self.head:
            print("📭 Playlist is empty.")
            return
        print("\n🎧 Current Playlist:")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.title}")
            current = current.next
            i += 1

    def remove_song(self, title):
        if not self.head:
            print("🚫 Playlist is empty, nothing to remove.")
            return
        if self.head.title == title:
            self.head = self.head.next
            print(f"❌ Removed '{title}' from the playlist.")
            return
        current = self.head
        while current.next and current.next.title != title:
            current = current.next
        if current.next:
            current.next = current.next.next
            print(f"❌ Removed '{title}' from the playlist.")
        else:
            print(f"⚠️ Song '{title}' not found.")

def main():
    playlist = Playlist()
    print("🎵 Welcome to the Playlist Manager!")

    while True:
        print("\nMENU:")
        print("1. Add song")
        print("2. Remove song")
        print("3. View playlist")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            title = input("Enter song title: ").strip()
            playlist.add_song(title)
        elif choice == "2":
            title = input("Enter song title to remove: ").strip()
            playlist.remove_song(title)
        elif choice == "3":
            playlist.display()
        elif choice == "4":
            print("\n👋 Goodbye! Enjoy your tunes 🎶")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
