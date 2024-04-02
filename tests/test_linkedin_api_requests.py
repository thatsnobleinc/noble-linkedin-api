import os
import sys
import pytest

from src.noble_linkedin_api import Linkedin
from src.noble_linkedin_api.utils.helpers import get_id_from_urn

TEST_LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME", "cameron.jordan@thatsnoble.com")
TEST_LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD", "Wordofmouth22")
TEST_PROFILE_ID = os.getenv("TEST_PROFILE_ID", "ACoAAAcLc-kBGrxZVGc1BYcF3trNSWWUXQUjswc")
TEST_PUBLIC_PROFILE_ID = os.getenv("TEST_PUBLIC_PROFILE_ID", "joshua-budman-7496b933")
TEST_CONVERSATION_ID = os.getenv("TEST_CONVERSATION_ID", "6419123050114375168")

REQUEST_HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.33 Safari/537.36",
    "accept-language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "x-li-lang": "en_US",
    "x-restli-protocol-version": "2.0.0",
    "csrf-token": "ajax:0835618877918092985",
}

if not (
    TEST_LINKEDIN_USERNAME
    and TEST_LINKEDIN_PASSWORD
    and TEST_PROFILE_ID
    and TEST_PUBLIC_PROFILE_ID
    and TEST_CONVERSATION_ID
):
    print("Test config incomplete. Exiting...")
    sys.exit()


@pytest.fixture(scope="module")
def linkedin():

    # CAM JORDAN
    proxy_string =  "t1q3o:kmkyo757@169.197.83.74:6006"
    j_session_id = '"ajax:7253057009125232270"'
    li_at = "AQEFAREBAAAAAA7aKHMAAAGOexwV9QAAAY6fKJn1TgAAtHVybjpsaTplbnRlcnByaXNlQXV0aFRva2VuOmVKeGpaQUFDZm1tWklCRE5OOCtUQjBRTFN6N29ZZ1F4NGhTUHFJTVpHa0UvVnpNd0FnQnozUWE4XnVybjpsaTplbnRlcnByaXNlUHJvZmlsZToodXJuOmxpOmVudGVycHJpc2VBY2NvdW50OjI1MzQzNDk2MiwyNDUyNTQ0MTIpXnVybjpsaTptZW1iZXI6MTAwMjQ2NDI3M56uzyP-qTb_7EWSv7JeNwSqhUBcopU3OtgLZyfMjq0KaY8rmXzYYXctZdbYaUMeXpsCQ4OU2n4Mg5qje3ftlXCy3w_Wn89NG4O6IaiRyzWjCOIk4iULRaoyNjUjLrP7i7XTJNzEoLJ6blQGBxYdm194pL6LfTnxJkq25hFPvggiZPCA12pWU8MXXolVOsqkFATRp1U; UserMatchHistory=AQIhLIUyJhRMLAAAAY58Gxo3bP6Vm-y8yezeSaTlujRjDOophyF3QhJYSel2cgekBUpuoTShQX2Czfxlkr6LxSpctUR-gmrUWyqbd-2GLWSix0_6YdiGFwIL1JrSJkhgobHxw9HQ0L-5FvG2droBu-XolAMs7N_MkHmMWmTrdQ3gJF8-Nyv1aCQkKgt5wpxSRFbnOO-15fh_xfOfsHgoZ9FYlGgj0JzTYTfJSevAaNwsyJfBbxgQTZvXSCf1X2ujY-qUArn6-wJIQjj-o6aiN2j5duAU3y5Mv1Oi2f8W6P7CM43uKuK795SsCgFr_go-Q83kg7k"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36"
    li_a = "AQJ2PTEmc2FsZXNfY2lkPTMyMDQ2Mjk4NiUzQSUzQTMyMDQ4MTM1NCUzQSUzQXRpZXIxJTNBJTNBMjUzNDM0OTYyurkENjcqnnQd4bOoWpOfvMfWFOU"
    # Elijiah Perez
    # proxy_string =  "proxy-server1.mirrorprofiles.com:8080"
    # j_session_id = '"ajax:0962794415086379039"'
    # li_at = "AQEDAUgtEWEBp4n-AAABjSJ8npIAAAGOdVYJiU4AcYs7aZlIIua3jQecGPV_uLAXTjwWoD78AJxutaybP2bmmBnMYqOusEHQDF43juE6zJxHcT4ISij77bSfeYiZjVsKfESWnZxQ06Hzu6hq5hfMcU__"
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36"

    #Me
    # proxy_string = "nssnzkvh:i4j9nvkq1rvv@45.196.63.230:6864"
    # j_session_id = '"ajax:1817260717050867186"'
    # li_at = "AQEFARABAAAAAA7XbxgAAAGOZpb7awAAAY6KwHw6TgAAs3VybjpsaTplbnRlcnByaXNlQXV0aFRva2VuOmVKeGpaQUFDdmpJMkp4RE5PeWZoRXBqL2JNc2pSaEFqeEVWNE9waWhzbEJCbTRFUkFLUkpCNGc9XnVybjpsaTplbnRlcnByaXNlUHJvZmlsZToodXJuOmxpOmVudGVycHJpc2VBY2NvdW50OjI0MjYxNTg3NCwyMjgzNTIyMTApXnVybjpsaTptZW1iZXI6MTE4MTkxMDgxJYaz5RNuuBdAuggs3e9bPt0OSa-ysEBPOLtql8rhBxAs_Xia1e4GgtJsbfrOCX1959kLPdOWvXSBYAoeYgRCKZ6vdXUBpObs0J4U90wCXJybe2aXHPq0GZ67hFuB80QbTP_FkMEbmFXs5BJ817Bdee8Gztu7lhQ6JMzKXzKmDsIlXJxLemRMRruhlWczXrqK0mCkGQ"
    # user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36"

    return Linkedin(
        session_cookie=li_at, proxy_string=proxy_string, j_session_id=j_session_id, user_agent=user_agent, li_a=li_a, debug=True
    )


def test_get_profile(linkedin):
    profile = linkedin.get_profile(public_id='joshua-budman-7496b933') #urn_id=TEST_PROFILE_ID)
    print(profile)
    assert profile


def test_view_profile(linkedin):
    err = linkedin.view_profile(TEST_PUBLIC_PROFILE_ID)

    assert not err


def test_get_profile_privacy_settings(linkedin):
    data = linkedin.get_profile_privacy_settings(TEST_PUBLIC_PROFILE_ID)

    assert data


def test_get_profile_member_badges(linkedin):
    data = linkedin.get_profile_member_badges(TEST_PUBLIC_PROFILE_ID)

    assert data


def test_get_profile_network_info(linkedin):
    data = linkedin.get_profile_network_info(TEST_PUBLIC_PROFILE_ID)

    assert data


def test_get_profile_contact_info(linkedin):
    contact_info = linkedin.get_profile_contact_info(TEST_PROFILE_ID)
    assert contact_info


def test_get_profile_connections(linkedin):
    connections = linkedin.get_profile_connections(TEST_PROFILE_ID)
    assert connections


def test_get_conversations(linkedin):
    conversations = linkedin.get_conversations()
    assert conversations


def test_get_conversation_details(linkedin):
    conversation_details = linkedin.get_conversation_details(TEST_PROFILE_ID)
    assert conversation_details


def test_get_conversation(linkedin):
    conversation = linkedin.get_conversation(TEST_CONVERSATION_ID)
    assert conversation


def test_send_message_to_conversation(linkedin):
    err = linkedin.send_message(
        conversation_urn_id=TEST_CONVERSATION_ID,
        message_body="test message from pytest",
    )
    assert not err


def test_send_message_to_recipients(linkedin):
    err = linkedin.send_message(
        recipients=[TEST_PROFILE_ID], message_body="test message from pytest"
    )
    assert not err


def test_mark_conversation_as_seen(linkedin):
    err = linkedin.mark_conversation_as_seen(TEST_CONVERSATION_ID)
    assert not err


def test_get_current_profile_views(linkedin):
    views = linkedin.get_current_profile_views()
    assert views >= 0


def test_get_school(linkedin):
    school = linkedin.get_school("university-of-queensland")
    assert school
    assert school["name"] == "The University of Queensland"


def test_get_company(linkedin):
    company = linkedin.get_company("linkedin")
    assert company
    assert company["name"] == "LinkedIn"


def test_search(linkedin):
    results = linkedin.search({"keywords": "software"})
    assert results


def test_search_pagination(linkedin):
    results = linkedin.search({"keywords": "software"}, limit=4)
    # according to implementation of functions search_people, search_companies
    # limit is valid within the category only. So in every category/type of test
    # the number of results shall not exceed a given limit
    numbers_in_categories = dict()
    for result in results:
        try:
            occurrence = numbers_in_categories[result["type"]]
        except KeyError:
            occurrence = 0
            numbers_in_categories.update({result["type"]: occurrence})
        occurrence += 1
        numbers_in_categories[result["type"]] = occurrence
    assert results
    assert max(numbers_in_categories.values()) == 4


def test_search_with_limit(linkedin):
    results = linkedin.search({"keywords": "tom"}, limit=1)
    assert len(results) == 1


def test_search_people(linkedin):
    results = linkedin.search_people(keywords="software", include_private_profiles=True)
    assert results


def test_search_people_with_limit(linkedin):
    results = linkedin.search_people(
        keywords="software", include_private_profiles=True, limit=1
    )
    assert results
    assert len(results) == 1


def test_search_people_by_region(linkedin):
    results = linkedin.search_people(
        keywords="software", include_private_profiles=True, regions=["105080838"]
    )
    assert results


def test_search_people_by_keywords_filter(linkedin: Linkedin):
    results, total_count = linkedin.search_people(
        connection_of='ACoAAAcLc-kBGrxZVGc1BYcF3trNSWWUXQUjswc',
        include_private_profiles=True, network_depths=['F','S'],
        current_company=['1277', '80823467', '120271', '11595','1033'],
        limit = 25, offset = 0
    )
    assert results
    assert total_count

def test_search_people_by_keywords_filter_navigator(linkedin: Linkedin):
    results, total_count = linkedin.search_people_navigator(
        connection_of='ACoAAAcLc-kBGrxZVGc1BYcF3trNSWWUXQUjswc',
        include_private_profiles=True,
        current_company_list=['1277', '80823467', '120271', '11595','1033'],
        limit = 25, offset = 0
    )

    assert results
    assert total_count

def test_search_jobs(linkedin):
    # test all filters for correct syntax
    # location_name -> "san francisco"
    # companies -> google="1441" or apple="162479"
    # experience ->"1", "2", "3", "4", "5" and "6" (internship, entry level, associate, mid-senior level, director and executive, respectively) 
    # job_type -> "F", "C", "P", "T", "I", "V", "O" (full-time, contract, part-time, temporary, internship, volunteer and "other", respectively)
    # job_title -> software_eng="9",cloud_eng="30006"
    # industries -> computer_hardware="24", it_technology="6"
    # distance -> big number 1000 miles
    # remote -> onsite:"1", remote:"2", hybrid:"3"
    # listed_at -> large number 1000000 seconds
    jobs = linkedin.search_jobs(
        keywords="software engineer",
        location_name="San Francisco",
        companies=["1441","162479"],
        experience=["1","2","3","4","5","6"],
        job_type=["F","C","P","T","I","V","O"],
        job_title=["9","30006"],
        industries=["24","6"],
        distance=1000,
        remote=["1","2","3"],
        listed_at=1000000,
        limit=10
    )
    assert len(jobs)==10

    # Test that no results doesn't return an infinite loop
    jobs = linkedin.search_jobs(
        keywords="blurp",
        location_name="antarctica"
    )
    assert len(jobs)==0


def test_get_job(linkedin):
    jobs = linkedin.search_jobs(
        keywords="software engineer",
        limit=1
    )
    job_id = get_id_from_urn(jobs[0]["trackingUrn"])
    job_info = linkedin.get_job(job_id)
    assert job_info


def test_search_companies(linkedin):
    results = linkedin.search_companies(keywords="linkedin", limit=1)
    assert results
    assert results[0]["urn_id"] == "1337"


# def test_search_people_distinct(linkedin):
#     TEST_NAMES = ['Bill Gates', 'Mark Zuckerberg']
#     results = [linkedin.search_people(name, limit=2)[0] for name in TEST_NAMES]
#     assert results[0] != results[1]


def test_get_profile_skills(linkedin):
    skills = linkedin.get_profile_skills(TEST_PROFILE_ID)
    assert skills


def test_get_invitiations(linkedin):
    invitations = linkedin.get_invitations()
    assert len(invitations) >= 0


def test_accept_invitation(linkedin):
    """
    NOTE: this test relies on the existence of invitations. If you'd like to test this
    functionality, make sure the test account has at least 1 invitation.
    """
    invitations = linkedin.get_invitations()
    if not invitations:
        # If we've got no invitations, just force test to pass
        assert True
        return
    num_invitations = len(invitations)
    invite = invitations[0]
    invitation_response = linkedin.reply_invitation(
        invitation_entity_urn=invite["entityUrn"],
        invitation_shared_secret=invite["sharedSecret"],
        action="accept",
    )
    assert invitation_response

    invitations = linkedin.get_invitations()
    assert len(invitations) == num_invitations - 1


def test_reject_invitation(linkedin):
    """
    NOTE: this test relies on the existence of invitations. If you'd like to test this
    functionality, make sure the test account has at least 1 invitation.
    """
    invitations = linkedin.get_invitations()
    if not invitations:
        # If we've got no invitations, just force test to pass
        assert True
        return
    num_invitations = len(invitations)
    invite = invitations[0]
    invitation_response = linkedin.reply_invitation(
        invitation_entity_urn=invite["entityUrn"],
        invitation_shared_secret=invite["sharedSecret"],
        action="reject",
    )
    assert invitation_response

    invitations = linkedin.get_invitations()
    assert len(invitations) == num_invitations - 1


def test_unfollow_entity(linkedin):
    urn = f"urn:li:member:ACoAACVmHBkBdk3IYY1uodl8Ht4W79rmdVFccOA"
    err = linkedin.unfollow_entity(urn)
    assert not err


def test_get_feed_posts_pagination(linkedin):
    results = linkedin.get_feed_posts(101)
    assert results


def test_get_feed_posts_pagination_with_limit(linkedin):
    results = linkedin.get_feed_posts(4)
    # Currently promotions are always removed from results
    assert len(results) <= 4


def test_get_feed_posts_posts_keys(linkedin):
    results = linkedin.get_feed_posts(4)
    for i in results:
        assert i["author_name"]
        assert i["author_profile"]
        assert i["content"]
        assert i["old"]
        assert i["url"]


def test_get_feed_posts_urns_contains_no_duplicated(linkedin):
    l_posts, l_urns = linkedin._get_list_feed_posts_and_list_feed_urns(101)
    assert len(set([x for x in l_urns if l_urns.count(x) > 1])) == 0


def test_is_request_accepted(linkedin):

    is_accepted = linkedin.is_request_accepted(first_name='James', last_name='Coll', li_url='https://www.linkedin.com/in/james-coll-9198b7165/')
    assert is_accepted

    # is_accepted = linkedin.is_request_accepted(first_name='jason', last_name='Widup', li_url='https://www.linkedin.com/in/jasonwidup')
    # assert is_accepted
    #
    # is_accepted = linkedin.is_request_accepted(first_name='Igor', last_name='mpore', li_url='https://www.linkedin.com/in/igormpore/')
    # assert is_accepted


def test_add_connection(linkedin):

    public_profile_id = 'cameronaubuchon'

    result = linkedin.add_connection(profile_public_id=public_profile_id)
    print(result)

    assert result

def test_convert_navigator_id(linkedin):
    navigator_id = 'ACwAAACvx6EBAyOcjFD55-q3m2mnvA1H9ceRaik'
    result = linkedin.convert_navigator_id_to_vanity(navigator_id=navigator_id)
    assert result