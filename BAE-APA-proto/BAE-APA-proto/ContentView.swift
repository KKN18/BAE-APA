//
//  ContentView.swift
//  BAE-APA-proto
//
//  Created by Seah Kim on 2023/06/29.
//

import SwiftUI

extension EdgeInsets {
  var horizontalInsets: CGFloat { self.trailing + self.leading }
  var verticalInsets: CGFloat { self.top + self.bottom }
  var left: CGFloat { self.leading }
  var right: CGFloat { self.trailing }
  
  static func with(top: CGFloat = 0, left: CGFloat = 0, bottom: CGFloat = 0, right: CGFloat = 0) -> EdgeInsets {
    EdgeInsets(top: top, leading: left, bottom: bottom, trailing: right)
  }

static func horizontal(_ horizontal: CGFloat, top: CGFloat = 0, bottom: CGFloat = 0) -> UIEdgeInsets {
  UIEdgeInsets(
    top: top,
    left: horizontal,
    bottom: bottom,
    right: horizontal
  )
}

static func vertical(_ vertical: CGFloat, left: CGFloat = 0, right: CGFloat = 0) -> UIEdgeInsets {
  UIEdgeInsets(
    top: vertical,
    left: left,
    bottom: vertical,
    right: right
  )
}

init(_ all: CGFloat) {
  self = EdgeInsets(top: all, leading: all, bottom: all, trailing: all)
}

init(top: CGFloat = 0, left: CGFloat = 0, bottom: CGFloat = 0, right: CGFloat = 0) {
  self = EdgeInsets(top: top, leading: left, bottom: bottom, trailing: right)
}

init(horizontal: CGFloat = 0, vertical: CGFloat = 0) {
  self = EdgeInsets(top: vertical, leading: horizontal, bottom: vertical, trailing: horizontal)
}

func with(left: CGFloat? = nil, right: CGFloat? = nil, top: CGFloat? = nil, bottom: CGFloat? = nil) -> UIEdgeInsets {
  UIEdgeInsets(
    top: top ?? self.top,
    left: left ?? self.left,
    bottom: bottom ?? self.bottom,
    right: right ?? self.right
  )
}

func with(horizontal: CGFloat, top: CGFloat? = nil, bottom: CGFloat? = nil) -> UIEdgeInsets {
  UIEdgeInsets(
    top: top ?? self.top,
    left: horizontal,
    bottom: bottom ?? self.bottom,
    right: horizontal
  )
}

func with(vertical: CGFloat, left: CGFloat? = nil, right: CGFloat? = nil) -> UIEdgeInsets {
  UIEdgeInsets(
    top: vertical,
    left: left ?? self.left,
    bottom: vertical,
    right: right ?? self.right
  )
}
  }

struct InsetRoundButton: ButtonStyle {
  var labelColor = Color.white
  var backgroundColor = Color.blue
  
  func makeBody(configuration: Configuration) -> some View {
    configuration.label
      .foregroundColor(labelColor)
      .padding(.init(horizontal: 20, vertical: 13))
      .background(Capsule().fill(backgroundColor))
  }
}

struct InsetRoundScaleButton: ButtonStyle {
  var labelColor = Color.white
  var backgroundColor = Color.blue
  
  func makeBody(configuration: Configuration) -> some View {
    configuration.label
      .foregroundColor(labelColor)
      .padding(.init(horizontal: 20, vertical: 13))
      .background(Capsule().fill(backgroundColor))
      .scaleEffect(configuration.isPressed ? 0.88 : 1.0)
  }
}


struct ContentView: View {
    @State private var pageIndex=0
    private let pages:[Page]=Page.samplePages
    private let dotApperance=UIPageControl.appearance()
    
    var body: some View {
        ZStack{
            LinearGradient(colors: [.white, Color(red: 255 / 255, green: 222 / 255, blue: 150/255)],
                                   startPoint: .top,
                           endPoint: .center).ignoresSafeArea()
            TabView(selection: $pageIndex){
                ForEach(pages) { page in
                    VStack{
                        if page==pages.last{
                            Spacer()
                            Spacer()
                            Text(page.name)
                                .font(.custom("Plump MT", size: 40))
                                .foregroundColor(.orange)
                                .fixedSize(horizontal: false, vertical: true)
                                .bold()
                                .offset(x: 0, y: 70)
                            Text(page.description)
                                .font(.subheadline)
                                .frame(width:400)
                                .fixedSize(horizontal: false, vertical: true)
                                .multilineTextAlignment(.center)
                                .offset(x: 0, y: 70)
                            ZStack {
                                RoundedRectangle(cornerRadius: 30)
                                        .fill(Color.white)
                                        .frame(width: 200, height: 200)
                                        .position(x: 195, y: 210)
                                Image("\(page.imageUrl)")
                                    .resizable()
                                    .scaledToFit()
                                    .frame(width: 150, height: 150)
                                    .position(x: 195, y: 210)
                            }
                            Text(page.member)
                                .font(.subheadline)
                                .bold()
                                .frame(width: 150)
                                .fixedSize(horizontal: false, vertical: true)
                                .offset(x: 0, y: -95)
                            Text(page.organization)
                                .font(.system(size: 13)) 
                                .fixedSize(horizontal: false, vertical: true)
                                .offset(x: 0, y: -90)
                            Text(page.date)
                                .font(.system(size: 13))
                                .offset(x: 0, y: -90)
                            Spacer(minLength: 3)
                            //.frame(width: 300)
                            Spacer()
                        }
                        else if page==pages.first{
                            ZStack {
                                Image("logo_back")
                                    .resizable()
                                    .scaledToFit()
                                    .frame(width: 130, height: 130)
                                    .padding()
                                    .offset(x: 0, y: 50)
                                Image("logo_png")
                                    .resizable()
                                    .scaledToFit()
                                    .frame(width: 130, height: 130)
                                    .padding()
                                    .offset(x: 0, y: 50)
                            }

                            Text(page.name)
                                .font(.custom("Plump MT", size: 30))
                                .foregroundColor(.orange)
                                .bold()
                                .offset(x:0, y:30)
//                                .multilineTextAlignment(.center)
                            //PageView(page: page)
                            Image("\(page.imageUrl)")
                                .resizable()
                                //.position(x:160, y:200)
                                .scaledToFit()
                                .padding()
                                .padding()
                                .offset(x:0, y:70)
                                .scaleEffect(1.5)
                            Text(page.organization)
                                .font(.system(size: 13))
                                .fixedSize(horizontal: false, vertical: true)
                                .offset(x:0, y:55)
                            Text(page.date)
                                .font(.system(size: 13))
                                .offset(x:0, y:55)
                            Spacer(minLength: 3)

                            //.frame(width: 300)
                            Spacer()
                            //if page==pages.last{
                            //  Button("", action: goToZero)
                            //                                .buttonStyle(InsetRoundScaleButton(labelColor: .white, backgroundColor: .blue))
                            //} else{
                            //  Button("시작하기", action: incrementPage)
                            //      .buttonStyle(InsetRoundScaleButton(labelColor: .white, backgroundColor: .blue))
                            //  }
                        }
                        else{
                            Spacer()
                            Spacer()
                            Text(page.name)
                                .font(.custom("Plump MT", size: 40))
                                .foregroundColor(.orange)
                                .bold()
//                                .shadow(color: .gray, radius: 3, x: 0, y: 0)
                            Text(page.description)
                                .font(.subheadline)
                                .frame(width:400)
                                .fixedSize(horizontal: false, vertical: true)
                                .multilineTextAlignment(.center)
                            //PageView(page: page)
                            Image("\(page.imageUrl)")
                                .resizable()
                                .position(x:160, y:190)
                                .scaledToFit()
                                .padding()
                                .padding()
                            Text(page.member)
                                .font(.subheadline)
                                .bold()
                                .frame(width: 150)
                                .fixedSize(horizontal: false, vertical: true)
                                .offset(x:0, y:-5)
                            Text(page.organization)
                                .font(.system(size: 13))
                                .fixedSize(horizontal: false, vertical: true)
                                .offset(x:0, y:-10)
                            Text(page.date)
                                .font(.system(size: 13))
                                .offset(x:0, y:-10)
                            Spacer(minLength: 3)

                            //.frame(width: 300)
                            Spacer()
                            //if page==pages.last{
                            //  Button("", action: goToZero)
                            //      .buttonStyle(InsetRoundScaleButton(labelColor: .white, backgroundColor: .blue))
                            //} else{
                            //  Button("시작하기", action: incrementPage)
                            //      .buttonStyle(InsetRoundScaleButton(labelColor: .white, backgroundColor: .blue))
                            //}
                        }
                    }
                .tag(page.tag)
                }
            }
        }
        .animation(.easeInOut, value: pageIndex)
        .tabViewStyle(.page)
        .indexViewStyle(.page(backgroundDisplayMode: .interactive))
        .onAppear{
            dotApperance.currentPageIndicatorTintColor = .orange
            dotApperance.pageIndicatorTintColor = .white
        }
    }
    func incrementPage(){
        pageIndex+=1
    }
    func goToZero(){
        pageIndex=0
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
