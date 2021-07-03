##############################################################################################################################
# L=["","1617643","743181"]
# print(L)
# for i in L:
#     if i=="":
#         L.remove(i)
#
# print(L)
##############################################################################################################################
# Use del L[index] - To delete the list element by index position
# Use L.remove(item_name) - To delete the list element by item name
##############################################################################################################################
L=["tc85181cai_us_project_creation()","tc93546cai_us_create_non_catalog_req()","ie_clear_cache()","test_approve_requisition()","ie_clear_cache()","tc93548cai_us_CreatePO()","tc98611cai_us_auto_create_po_validation_1()","tc16319cai_us_ReceivePoItems()","ie_clear_cache()","tc98612cai_us_CorrectReceipt()","ie_clear_cache()","tc84510cai_us_create_manual_ap_invoice_match()","tc93849cai_us_create_accounting()","ie_clear_cache()","tc98616cai_us_ap_invoices_initiate_approval()","ie_clear_cache()","tc95047cai_us_validate_subledger_accounting()","tc93848cai_us_next_day_check_payment()","ie_clear_cache()","tc93850cai_us_journal_validation()","ie_clear_cache()","tc97359cai_us_cai_pa_nightly_request_set()","tc97750cai_us_create_project_asset()","tc93484cai_us_prc_generate_asset_lines_for_a_single_project()","ie_clear_cache()","tc93485cai_us_prc_interface_assets_to_oracle_assets()","tc93507cai_us_post_mass_additions()","tc99685cai_us_asset_inquiry()","tc97761cai_us_asset_tieback()"]

# for i in L:
#     if i == "ie_clear_cache()":
#         L.remove(i)
#
[L.remove(i) for i in L if i == "ie_clear_cache()"]  # Using List Comprehension

#

for i in L:
    print(i)

# for i in range(20):
#     print(len(L))
#
#     if L[i]=="ie_clear_cache()":
#        del L[i]
#     print(len(L))