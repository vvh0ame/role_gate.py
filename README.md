# role_gate.js
Mobile-API for [RoleGate](https://play.google.com/store/apps/details?id=com.LodestarTeam.rolegateapp) an platform to play any tabletop RPG by chat

## Example
```JavaScript
async function main() {
	const { RoleGate } = require("./role_gate.js")
	const roleGate = new RoleGate()
	await roleGate.login("username", "password")
}

main()
```
