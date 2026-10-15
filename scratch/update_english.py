"""
Update site-complete/info/english.html
to include the complete seminar details from the mirror,
while preserving the dark theme and elegant typography.
"""
import re

with open(r'site-complete\info\english.html', 'r', encoding='utf-8') as f:
    template = f.read()

seminar_section = '''<section class="materials" id="moreinfo">
<h2>International Seminar of Budo Culture</h2>
<p class="lead">INFORMATION: The 19th International Seminar of Budo Culture</p>
<table class="info-tbl" style="width:100%;margin-top:16px;border-collapse:collapse;font-size:0.95rem">
<tbody>
<tr><th style="width:28%;padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">1. Objectives</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">This seminar, aimed at foreign budo practitioners who live in Japan, is designed to deepen the understanding of historical philosophic and scientific aspects of budo to increase our mutual friendship and internationalize our traditional culture. This seminar will also teach the theories and techniques of budo.</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">2. Organizer</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">Nippon Budokan Foundation</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">3. Supported by</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">Ministry of Education, Culture, Sports, Science and Technology<br>Japanese Budo Association</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">4. With cooperation of</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">International Budo University</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">5. Dates</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">Friday, March 2 to Monday, March 5, 2007 (Four days three nights)<br><small class="quiet">Participants are expected to arrange their own transportation to and from Katsuura Training Center.</small></td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">6. Place of seminar</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">International Budo University (841 Shinga, Katsuura City, Chiba Prefecture Tel 0470-73-4111)<br>Nippon Budokan Training Center (582 Sawakura, Katsuura City, Chiba Prefecture Tel 0470-73-2111)<br>Accommodation: Nippon Budokan Training Center</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">7. Conditions for acceptance</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">(1) Applicants must be foreign practitioners of modern budo over 18 and be resident in Japan. They must, in principle, have obtained shodan, at least.<br>(2) Applicants must understand either English or Japanese. (Both languages will be used during the seminar.)<br>(3) Applicants must, in principle, be recommended by an organization belonging to the Japanese Budo Association. Alternatively they must belong to a university or company budo club, and must be recommended by its leader.</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">8. Number of participants</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">100 (In principle, first time participants will be given preference if the number of applicants exceeds the limit.)</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">9. Application</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">Fill out the separate <a href="../pdf/info/english_isbc061227.pdf" style="color:var(--accent);text-decoration:underline">application form (PDF)</a> and send it with the fee to Nippon Budokan Foundation.<br>Participation fee: 5,250 yen (include tax) (Send by Registered Mail - Genkin Kakitome)<br>Only Japanese Yen will be accepted.<br>Send to: Nippon Budokan Promotions Department, 2-3, Kitanomaru-Koen, Chiyoda-ku, Tokyo 102-8321</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">10. Financial assistance</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">The organizers will be responsible for accommodation and meals during the seminar at the designated accommodation facility. Participants must pay their own travel expenses.</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">11. Insurance</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">(1) The Shiota Hospital in Katsuura has pledged their assistance in the event of an accident during the seminar.<br>(2) All participants will be covered by an insurance policy taken out by the Nippon Budokan. (Travel to and from the seminar venue is not included.)</td></tr>
<tr><th style="padding:12px;border:1px solid var(--line);text-align:left;vertical-align:top">12. Address inquiries to</th><td style="padding:12px;border:1px solid var(--line);line-height:1.8">Nippon Budokan Promotions Department<br>2-3, Kitanomaru-Koen, Chiyoda-ku, Tokyo 102-8321<br>TEL (03) 3216-5134 FAX (03) 3216-5117<br>10:00 to 17:00 except on Saturdays, Sundays, and public holidays.</td></tr>
</tbody>
</table>
<p class="quiet hint" style="margin-top:12px">* Please pass this information to any foreign friends practicing budo.</p>
</section>'''

# Insert seminar_section right before <p class="source">
new_content = template.replace('<p class="source">', seminar_section + '\n<p class="source">')

with open(r'site-complete\info\english.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated site-complete/info/english.html with seminar details!")
