def footer():
    delivery_laptop = '#rec868359447'
    return_laptop = '#rec868359448'
    delivery_mobile = '#rec868359456'
    return_mobile = '#rec868359457'
    mobile_footer = '#rec868359459'
    laptop_footer = '#rec868359453'
    print(
        delivery_laptop + ' .tn-elem[data-elem-id="1733663461139"],\n' +
        return_laptop + ' .tn-elem[data-elem-id="1733667145150"],\n' +
        delivery_mobile + ' .tn-elem[data-elem-id="1735470956772"],\n' +
        return_mobile + ' .tn-elem[data-elem-id="1735470956772"] {\n'
    )

    print(delivery_laptop + '[data-record-type="396"],\n' +
          return_laptop + '[data-record-type="396"],\n' +
          delivery_mobile + '[data-record-type="396"],\n' +
          return_mobile + '[data-record-type="396"] {\n')

    print(delivery_laptop + '[data-record-type="396"].popup-active,\n' +
          return_laptop + '[data-record-type="396"].popup-active,\n' +
          delivery_mobile + '[data-record-type="396"].popup-active,\n' +
          return_mobile + '[data-record-type="396"].popup-active {\n')

    # deliveryPopupTrigger = document.querySelector('#rec845818286 .tn-elem[data-elem-id="1733124053379"]');
    # returnPopupTrigger = document.querySelector('#rec845818286 .tn-elem[data-elem-id="1733124107459"]');
    #
    # deliveryPopup = document.querySelector('#rec846520156[data-record-type="396"]');
    # returnPopup = document.querySelector('#rec847142102[data-record-type="396"]');
    #
    # deliveryPopupBox = document.querySelector('#rec846520156 .tn-elem[data-elem-id="1733341154740"]');
    # returnPopupBox = document.querySelector('#rec847142102 .tn-elem[data-elem-id="1733341154740"]');
    print(
        f"deliveryPopupTrigger = document.querySelector('{mobile_footer} .tn-elem[data-elem-id=\"1733124053379\"]');\n" +
        f"\t\treturnPopupTrigger = document.querySelector('{mobile_footer} .tn-elem[data-elem-id=\"1733124107459\"]');\n\n" +
        f"\t\tdeliveryPopup = document.querySelector('{delivery_mobile}[data-record-type=\"396\"]');\n" +
        f"\t\treturnPopup = document.querySelector('{return_mobile}[data-record-type=\"396\"]');\n\n" +
        f"\t\tdeliveryPopupBox = document.querySelector('{delivery_mobile} .tn-elem[data-elem-id=\"1733341154740\"]');\n" +
        f"\t\treturnPopupBox = document.querySelector('{return_mobile} .tn-elem[data-elem-id=\"1733341154740\"]');\n")

    print(
        f"deliveryPopupTrigger = document.querySelector('{laptop_footer} .tn-elem[data-elem-id=\"1733124053379\"]');\n" +
        f"\t\treturnPopupTrigger = document.querySelector('{laptop_footer} .tn-elem[data-elem-id=\"1733124107459\"]');\n\n" +
        f"\t\tdeliveryPopup = document.querySelector('{delivery_laptop}[data-record-type=\"396\"]');\n" +
        f"\t\treturnPopup = document.querySelector('{return_laptop}[data-record-type=\"396\"]');\n\n" +
        f"\t\tdeliveryPopupBox = document.querySelector('{delivery_laptop} .tn-elem[data-elem-id=\"1733341154740\"]');\n" +
        f"\t\treturnPopupBox = document.querySelector('{return_laptop} .tn-elem[data-elem-id=\"1733667145063\"]');\n")

    print(f"{laptop_footer} .tn-elem[data-elem-id=\"1733124053379\"],\n" +
          f"{laptop_footer} .tn-elem[data-elem-id=\"1733124107459\"]" + " {" + "\ncursor: pointer;" + "\n}")


def db():
    who_to_put = [8, 13, 14, 17, 19, 22, 69]
    for i in who_to_put:
        print("{ id: " + '"' + str(i) + '", frontImage: '
              + '"", backImage: "https://static.tildacdn.com/tild3738-3862-4037-a466-343762666265/card_z.png", ' +
                f'joinDate: "since ", nickname: "{i}"'
              + " },")


db()