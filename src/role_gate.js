class RoleGate {
	constructor() {
		this.api = "https://www.rolegate.com"
		this.headers = {
			"user-agent": "okhttp/3.14.9"
		}
	}

	async register(username, email, password) {
		const response = await fetch(
			`${this.api}/account/signup`, {
				method: "POST",
				body: JSON.stringify({
					username: username,
					password: password,
					password2: password,
					email: email
				}),
				headers: this.headers
			})
		return response.json()
	}

	async login(username, password) {
		const response = await fetch(
			`${this.api}/api/v2/api-token-auth`, {
				method: "POST",
				body: JSON.stringify({
					username: username,
					password: password
				}),
				headers: this.headers
			})
		const data = await response.json()
		if ("token" in data) {
			this.token = data.token
			this.headers["authorization"] = `Token ${this.token}`
			this.userId = await this.getCurrentUser().profile.id
		}
		return data
	}

	async getCurrentUser() {
		const response = await fetch(
			`${this.api}/api/v2/users/current`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAvatars() {
		const response = await fetch(
			`${this.api}/api/v2/avatars`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserTransactions(userId, ordering = "date", pageSize = 50) {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}/coin-transactions?ordering=-${ordering}&page-size=${pageSize}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserReferringCount(userId) {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}/profiles-referring-count`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserGameAlerts(userId) {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}/game-alerts`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserBookmarks(userId, ordering = "date") {
		const response = await fetch(
			`${this.api}/api/v2/users/${userId}/games?ordering=-$${ordering}&bookmarked=True`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getFeaturedGames() {
		const response = await fetch(
			`${this.api}/api/v2/games/featured-games`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGameInfo(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGameCharacters(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}/characters`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGamePreviewSelection(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}/lines/preview-selection`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGameStates(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}/states`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGameSheets(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}/sheets`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGameTokens(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}/tokens`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGameDiceSets(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}/dice-sets`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async gerRecommendedTags() {
		const response = await fetch(
			`${this.api}/api/v2/recommended-tags`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGames(page, isHidden = false) {
		const response = await fetch(
			`${this.api}/api/v2/games?hidden=${isHidden}&page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async joinGame(
			gameId,
			characterName,
			portraitAvatar = null,
			color = 1,
			isNpc = false) {
		let body = {
			color: color,
			background_color: 1,
			background_rank: "no",
			background_key: 0,
			"player-id": this.userId,
			npc: isNpc,
			"character-name": characterName
		}
		if (portraitAvatar) {
			body.portrait_avatar = portraitAvatar
		}
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}/characters`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}

	async leaveGame(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/users/${this.userId}/games/${gameId}/leave`, {
				method: "POST",
				headers: this.headers
			})
		return response.status_code
	}

	async createGame(
			name,
			description,
			rules,
			cover,
			sheetId,
			publicTemplateId,
			expectedPace = 0,
			isHidden = false,
			allowSpectators = true,
			allowPublicChat = true,
			maxPlayers = 4,
			password = null,
			tags = [],
			diceSets = [1]) {
		const response = await fetch(
			`${this.api}/api/v2/games`, {
				method: "POST",
				body: JSON.stringify({
					expected_pace: expectedPace,
					hidden: isHidden,
					allow_spectators: allowSpectators,
					allow_public_chat: allowPublicChat,
					max_players: maxPlayers,
					name: name,
					description: description,
					rules: rules,
					password: password,
					cover: cover,
					sheet: sheetId,
					tags: tags,
					dice_sets: diceSets,
					public_template: publicTemplateId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getBackgrounds(pageSize = 100) {
		const response = await fetch(
			`${this.api}/api/v2/stage-backgrounds?page-size=${pageSize}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getSheets(isPublic = true) {
		const response = await fetch(
			`${this.api}/api/v2/sheets?public=${isPublic}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async deleteGame(gameId) {
		const response = await fetch(
			`${this.api}/api/v2/games/${gameId}`, {
				method: "DELETE",
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {RoleGate}
