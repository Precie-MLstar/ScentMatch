
const discoverButton = document.querySelector("#discoverBtn");
const result = document.querySelector("#result");

const scentProfiles = [
    {
        name: "The Romantic Florist",
        notes: "Soft, luminous florals with a graceful, feminine feel.",
        perfumes: ["Chanel Chance Eau Tendre", "Marc Jacobs Daisy"],
    },
    {
        name: "The Warm Sophisticate",
        notes: "Rich woods, amber, and a little smoky depth.",
        perfumes: ["Yves Saint Laurent Libre", "Maison Margiela Replica By the Fireplace"],
    },
    {
        name: "The Sweet Dreamer",
        notes: "Comforting vanilla and delicious gourmand notes.",
        perfumes: ["Burberry Goddess", "Prada Candy"],
    },
    {
        name: "The Fresh Minimalist",
        notes: "Clean citrus and airy notes that feel bright and effortless.",
        perfumes: ["Dolce & Gabbana Light Blue", "Jo Malone Wood Sage & Sea Salt"],
    },
];

let previousProfileIndex = -1;

if (discoverButton && result) {
    discoverButton.addEventListener("click", () => {
        let profileIndex = Math.floor(Math.random() * scentProfiles.length);

        while (scentProfiles.length > 1 && profileIndex === previousProfileIndex) {
            profileIndex = Math.floor(Math.random() * scentProfiles.length);
        }

        previousProfileIndex = profileIndex;
        const profile = scentProfiles[profileIndex];
        const card = document.createElement("article");
        const label = document.createElement("p");
        const heading = document.createElement("h2");
        const description = document.createElement("p");
        const suggestionHeading = document.createElement("h3");
        const perfumeList = document.createElement("ul");

        card.className = "profile-card";
        label.className = "profile-label";
        label.textContent = "YOUR SCENT PROFILE";
        heading.textContent = profile.name;
        description.textContent = profile.notes;
        suggestionHeading.textContent = "Perfumes to explore";

        profile.perfumes.forEach((perfume) => {
            const item = document.createElement("li");
            item.textContent = perfume;
            perfumeList.append(item);
        });

        card.append(label, heading, description, suggestionHeading, perfumeList);
        result.replaceChildren(card);
        discoverButton.textContent = "DISCOVER ANOTHER PROFILE ↗";
    });
}

