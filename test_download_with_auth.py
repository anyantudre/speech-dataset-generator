from pytubefix import YouTube

url = input("url >")

yt = YouTube(url, use_po_token=True)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()



po= "MluJWXBRjNdA64lh_5oQ00YVDwX_gIImNLQMkU61iC-TqRO-DVGfDVLrF49OJjAd3ZtQUkMv2Hn99-5RcfaFY63c19OwHQw1om27fyNq0NWp_JKwqAS7Gf_T72-y"
visitorData= "CgtPaEI4YmNENEZETSig2tO4BjIKCgJNQRIEGgAgJw%3D%3D"