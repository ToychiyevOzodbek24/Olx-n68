from apps.posts.utils import PostQueries


class PostMenu(PostQueries):
    def show_posts(self):
        posts = self.get_all_posts()
        print("\nAvailable Posts:")
        if not posts:
            print("No posts available.")
        else:
            for post in posts:
                print(f"{post['id']}. {post['title']} - ${post['price']} | Active: {post['is_active']}")

    def add_post(self):
        title = input("Enter post title: ")
        description = input("Enter post description: ")
        try:
            price = int(input("Enter price: "))
            if self.insert_post(title, description, price):
                print("Post added successfully.")
            else:
                print("Failed to add post.")
        except ValueError:
            print("Invalid price.")

    def delete_post(self):
        try:
            post_id = int(input("Enter post ID to delete: "))
            if self.delete_post_by_id(post_id):
                print("Post deleted.")
            else:
                print("Post not found.")
        except ValueError:
            print("Invalid input.")

    def update_post(self):
        try:
            post_id = int(input("Enter post ID to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            price = int(input("Enter new price: "))
            is_active = input("Is active? (yes/no): ").lower() == "yes"
            if self.update_post_by_id(post_id, title, description, price, is_active):
                print("Post updated.")
            else:
                print("Post not found.")
        except ValueError:
            print("Invalid input.")