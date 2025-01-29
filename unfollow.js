(async function () {
    console.log("Début du script pour Unfollow sur LinkedIn...");

    let totalUnfollowed = 0;

    async function scrollToLoadAllFollowers() {
        console.log("Chargement des abonnements...");
        let previousHeight = 0;
        let retries = 0;

        while (true) {
            window.scrollBy(0, 1000);
            await new Promise(r => setTimeout(r, 500));

            let newHeight = document.body.scrollHeight;
            if (newHeight === previousHeight) {
                retries++;
                if (retries >= 3) break;
            } else {
                retries = 0;
            }
            previousHeight = newHeight;
        }
        console.log("Tous les abonnements ont été chargés.");
    }

    async function unfollowProfiles() {
        let profiles = document.querySelectorAll('button[aria-label^="Ne plus suivre"]');
        
        for (let btn of profiles) {
            btn.click();
            console.log(`Unfollowed: ${btn.getAttribute('aria-label')}`);
            totalUnfollowed++;
            await new Promise(r => setTimeout(r, 1000)); 
        }
    }

    await scrollToLoadAllFollowers();
    await unfollowProfiles();

    console.log(`Script terminé. Total de comptes Unfollow : ${totalUnfollowed}`);
})();
