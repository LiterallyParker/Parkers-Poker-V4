const naughtyList = [
    /\bass\b/i, /\bbitch\b/i, /\bbastard\b/i, /\bfuck\b/i, /\bshit\b/i,
    /\bdamn\b/i, /\bhell\b/i, /\bcunt\b/i, /\bcock\b/i, /\bpussy\b/i,
    /\bdick\b/i, /\bfag\b/i, /\bslut\b/i, /\bwhore\b/i, /\bbimbo\b/i,
    /\bretard\b/i, /\bidiot\b/i, /\bmoron\b/i, /\bfucker\b/i, /\basshole\b/i,
    /\bprick\b/i, /\bdouche\b/i, /\btwat\b/i, /\btits\b/i, /\bballs\b/i,
    /\bcum\b/i, /\bpiss\b/i, /nigger/i, /\bspic\b/i, /\bchink\b/i,
    /\bkike\b/i, /\bgypsy\b/i, /\bcracker\b/i, /\bwetback\b/i,
    /\bslanteye\b/i, /\bbeaner\b/i, /\bfaggot\b/i, /\btranny\b/i, /\bbitchass\b/i,
    /\bshithead\b/i, /\bcockhead\b/i, /\bdouchebag\b/i, /\bshitstain\b/i,
    /\basswipe\b/i, /\bmotherfucker\b/i, /\bcocksucker\b/i, /\bdickhead\b/i,
    /\bcuntface\b/i, /\bbitchslap\b/i, /\bdicknose\b/i, /\bbuttplug\b/i,
    /\bskank\b/i, /\bho\b/i, /\bjackass\b/i, /\bprickface\b/i, /\bpenis\b/i,
    /\bvagina\b/i, /\bmotherfucking\b/i, /\basshat\b/i, /\bassclown\b/i,
    /\bbastardization\b/i, /\bcumshot\b/i, /\bporn\b/i, /\bsex\b/i,
    /\bfisting\b/i, /\bincest\b/i, /\brape\b/i, /\bpedophile\b/i,
    /\bmolestation\b/i, /\bbestiality\b/i, /\bcuck\b/i, /\bwank\b/i,
    /\bsmegma\b/i, /\bteabag\b/i, /\bsuck\bmy\b/i, /\bblowjob\b/i, /\bsuck\bit\b/i
]; // Yikes!

const isProfane = (word) => {
    return naughtyList.some((regex) => regex.test(word));
};
 
module.exports = isProfane