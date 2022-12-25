import requests

class RoleGate:
	def __init__(self) -> None:
		self.api = "https://www.rolegate.com"
		self.headers = {
			"user-agent": "okhttp/3.14.9"
		}
		self.token = None
		self.user_id = None

	def register(
			self,
			username: str,
			email: str,
			password: str) -> dict:
		data = {
			"username": username,
			"password": password,
			"password2": password,
			"email": email,
		}
		return requests.post(
			f"{self.api}/account/signup",
			data=data,
			headers=self.headers).json()

	def login(
			self,
			username: str,
			password: str) -> dict:
		data = {
			"username": username,
			"password": password
		}
		response = requests.post(
			f"{self.api}/api/v2/api-token-auth",
			data=data,
			headers=self.headers).json()
		if "token" in response:
			self.token = response["token"]
			self.headers["authorization"] = f"Token {self.token}"
			self.user_id = self.get_current_user()["profile"]["id"]
		return response

	def get_current_user(self) -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/current",
			headers=self.headers).json()

	def get_avatars(self) -> dict:
		return requests.get(
			f"{self.api}/api/v2/avatars",
			headers=self.headers).json()

	def get_user_transactions(
			self,
			user_id: int,
			ordering: str = "date",
			page_size: int = 50) -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/{user_id}/coin-transactions?ordering=-{ordering}&page-size={page_size}",
			headers=self.headers).json()

	def get_user_referring_count(
			self, 
			user_id: int) -> int:
		return requests.get(
			f"{self.api}/api/v2/users/{user_id}/profiles-referring-count",
			headers=self.headers).text

	def get_user_game_alerts(
			self,
			user_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/{user_id}/game-alerts",
			headers=self.headers).json()

	def get_user_bookmarks(
			self,
			user_id: int,
			ordering: str = "last_update") -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/{user_id}/games?ordering=-{ordering}&bookmarked=True",
			headers=self.headers).json()

	def get_featured_games(self) -> list:
		return requests.get(
			F"{self.api}/api/v2/games/featured-games",
			headers=self.headers).json()

	def get_game_info(self, game_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games/{game_id}",
			headers=self.headers).json()

	def get_game_characters(
			self,
			game_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games/{game_id}/characters",
			headers=self.headers).json()

	def get_game_preview_selection(
			self,
			game_id: int) -> list:
		return requests.get(
			f"{self.api}/api/v2/games/{game_id}/lines/preview-selection",
			headers=self.headers).json()

	def get_game_states(
			self,
			game_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games/{game_id}/states",
			headers=self.headers).json()

	def get_game_sheets(
			self,
			game_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games/{game_id}/sheets",
			headers=self.headers).json()

	def get_game_tokens(
			self,
			game_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games/{game_id}/tokens",
			headers=self.headers).json()

	def get_game_dice_sets(
			self,
			game_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games/{game_id}/dice-sets",
			headers=self.headers).json()

	def get_recommended_tags(self) -> list:
		return requests.get(
			f"{self.api}/api/v2/tags/recommended-tags",
			headers=self.headers).json()

	def get_games_by_tag(
			self,
			tag_id: int,
			page_size: int = 10) -> dict:
		return requests.get(
			f"{self.api}/api/v2/tags/{tag_id}/games?page-size={page_size}",
			headers=self.headers).json()

	def get_games(
			self,
			page: int,
			is_hidden: bool = False) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games?hidden={is_hidden}&page={page}",
			headers=self.headers).json()

	def join_game(
			self,
			character_name: str,
			portrait_avatar: str = None,
			color: int = 1,
			is_npc: bool = False) -> dict:
		data = {
			"color": color,
			"background_color": 1,
			"background_rank": "no",
			"background_key": 0,
			"player-id": self.user_id,
			"npc": is_npc,
			"character-name": character_name
		}
		if portrait_avatar:
			data["portrait_avatar"] = portrait_avatar
		return requests.post(
			f"{self.api}/api/v2/games/{game_id}/characters",
			data=data,
			headers=self.headers).json()

	def leave_game(
			self,
			game_id: int) -> int:
		return requests.post(
			f"{self.api}/api/v2/users/{self.user_id}/games/{game_id}/leave",
			headers=self.headers).status_code

	def search_game(
			self,
			query: str,
			page: int = 1,
			is_hidden: bool = False) -> dict:
		return requests.get(
			f"{self.api}/api/v2/games?hidden={is_hidden}&page={page}&search={query}",
			headers=self.headers).json()

	def get_backgrounds(
			self,
			page_size: int = 100) -> dict:
		return requests.get(
			f"{self.api}/api/v2/stage-backgrounds?page-size={page_size}",
			headers=self.headers).json()

	def get_sheets(
			self,
			is_public: bool = True) -> dict:
		return requests.get(
			f"{self.api}/api/v2/sheets?public={is_public}",
			headers=self.headers).json()

	def create_game(
			self,
			name: str,
			description: str,
			rules: str,
			cover: str,
			sheet_id: int,
			public_template_id: int,
			expected_pace: int = 0,
			is_hidden: bool = False,
			allow_spectators: bool = True,
			allow_public_chat: bool = True,
			max_players: int = 4,
			password: str = None,
			tags: list = [],
			dice_sets: list = [1]) -> dict:
		data = {
			"expected_pace": expected_pace,
			"hidden": is_hidden,
			"allow_spectators": allow_spectators,
			"allow_public_chat": allow_public_chat,
			"max_players": max_players,
			"name": name,
			"description": description,
			"rules": rules,
			"password": password,
			"cover": cover,
			"sheet": sheet_id,
			"tags": tags,
			"dice_sets": dice_sets,
			"public_template": public_template_id
		}
		return requests.post(
			f"{self.api}/api/v2/games",
			data=data,
			headers=self.headers).json()


	def get_sheet_info(self, sheet_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/v2/sheets/{sheet_id}",
			headers=self.headers).json()

	def get_sheet_nodes(self, sheet_id: int) -> list:
		return requests.get(
			f"{self.api}/api/v2/sheets/{sheet_id}/nodes",
			headers=self.headers).json()

	def get_sheet_tabs(self, sheet_id: int) -> list:
		return requests.get(
			f"{self.api}/api/v2/sheets/{sheet_id}/tabs",
			headers=self.headers).json()

	def edit_game(
			self,
			game_id: int,
			name: str = None,
			description: str = None,
			rules: str = None,
			password: str = None,
			tags: list = None,
			max_players: int = None,
			expected_pace: int = None,
			beginner_friendly: bool = True,
			allow_spectators: bool = True,
			allow_public_chat: bool = True,
			allow_export: bool = False,
			is_hidden: bool = False) -> dict:
		data = {}
		if name:
			data["name"] = name
		if description:
			data["description"] = description
		if rules:
			data["rules"] = rules
		if password:
			data["password"] = password
		if tags:
			data["tags"] = tags
		if max_players:
			data["max_players"] = max_players
		if expected_pace:
			data["expected_pace"] = expected_pace
		if beginner_friendly:
			data["beginner_friendly"] = beginner_friendly
		if allow_spectators:
			data["allow_spectators"] = allow_spectators
		if allow_public_chat:
			data["allow_public_chat"] = allow_public_chat
		if allow_export:
			data["allow_export"] = allow_export
		if is_hidden:
			data["hidden"] = is_hidden
		return requests.patch(
			f"{self.api}/api/v2/games/{game_id}",
			data=data,
			headers=self.headers).json()

	def delete_game(self, game_id: int) -> int:
		return requests.delete(
			f"{self.api}/api/v2/games/{game_id}",
			headers=self.headers).status_code

	def get_message_groups(self) -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/{self.user_id}/message-groups",
			headers=self.headers).json()

	def search_message_group(self, query: str) -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/{self.user_id}/message-groups?search={query}",
			headers=self.headers).json()	

	def get_friend_requests(self) -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/{self.user_id}/friend-requests?receiver_id={self.user_id}",
			headers=self.headers).json()

	def get_user_profile(self, username: str) -> dict:
		return requests.get(
			f"{self.api}/api/v2/users/{username}",
			headers=self.headears).json()

	def change_email(self, email: str) -> dict:
		data = {
			"email": email
		}
		return requests.patch(
			f"{self.api}/api/v2/profiles/{self.user_id}",
			data=data,
			headers=self.headers).json()

	def delete_account(self) -> int:
		return requests.delete(
			f"{self.api}/api/v2/profiles/{self.user_id}",
			headers=self.headers).status_code
