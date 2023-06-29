//
//  PageModel.swift
//  BAE-APA-proto
//
//  Created by Seah Kim on 2023/06/29.
//

import Foundation

struct Page: Identifiable, Equatable{
    let id=UUID()
    var name: String
    var description: String
    var imageUrl: String
    var member: String
    var organization: String
    var date: String
    var tag: Int
    
    static var samplePage=Page(name: "Title Example", description:"", imageUrl: "work", member: "member1 member2 member3 member4 member5 member6", organization: "2023 SW 중심대학 해커톤", date: "yyyy.mm.dd~yyyy.mm.dd", tag: 0)
    
    static var samplePages: [Page]=[
        Page(name: "BAE-APA?", description:"logo_main", imageUrl: "daejang", member: "\n\n\n\n김기남 김세아 노서준 정성문 정세연 정현태\n\n", organization: "©2023 SW 중심대학 해커톤 39 BAE-GOPA", date: "2023.06.28.~2023.06.30.", tag: 0),
        Page(name: "BAE-APA?", description:"AI Food Identification을 활용하여\n위장관계 질병을 예방∙치료하기 위한 주의 식품 알리미", imageUrl: "wc_daejang", member: "\n김기남 김세아 노서준 정성문 정세연 정현태\n\n", organization: "\n©2023 SW 중심대학 해커톤 39 BAE-GOPA", date: "2023.06.28.~2023.06.30.", tag: 1),
        Page(name: "BAE-APA?", description:"AI Food Identification을 활용하여\n위장관계 질병을 예방∙치료하기 위한 주의 식품 알리미\n", imageUrl: "logo_png", member: "김기남 김세아 노서준 정성문 정세연 정현태\n\n", organization: "©2023 SW 중심대학 해커톤 39 BAE-GOPA", date: "2023.06.28.~2023.06.30.", tag: 2)
    ]
}
