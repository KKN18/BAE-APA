//
//  ViewController.swift
//  TestTabBar
//
//  Created by Seah Kim on 2023/06/30.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let gradientLayer = CAGradientLayer()
            gradientLayer.frame = view.bounds
            gradientLayer.colors = [UIColor.white.cgColor, UIColor(red: 255/255, green: 139/255, blue: 56/255, alpha: 1).cgColor]
        gradientLayer.startPoint = CGPoint(x: 0.5, y: 0.5)
        gradientLayer.endPoint = CGPoint(x: 0.5, y: 0)

            view.layer.insertSublayer(gradientLayer, at: 0)
    
        
        if let image1 = UIImage(named: "daejang_hell")?.cgImage {
            let imageLayer1 = CALayer()
            imageLayer1.contents = image1
            imageLayer1.frame = CGRect(x: 0, y: -190, width: view.bounds.width, height: view.bounds.height)
            imageLayer1.contentsGravity = .resizeAspect
            
            view.layer.addSublayer(imageLayer1)
        }
        
        // 두 번째 이미지 추가
        if let image2 = UIImage(named: "bar")?.cgImage {
            let imageLayer2 = CALayer()
            imageLayer2.contents = image2
            imageLayer2.frame = CGRect(x: 0, y: 200, width: view.bounds.width, height: view.bounds.height)
            imageLayer2.contentsGravity = .resizeAspect
            
            view.layer.addSublayer(imageLayer2)
        }
        
        let textLabel1 = UILabel(frame: CGRect(x: 0, y: -25, width: view.bounds.width, height: view.bounds.height))
        textLabel1.text = "체력 3단계"
        textLabel1.textColor = UIColor.black
        textLabel1.textAlignment = .center
        textLabel1.font = UIFont.boldSystemFont(ofSize: 15)

        view.addSubview(textLabel1)
        
        let textLabel = UILabel(frame: CGRect(x: 0, y: 10, width: view.bounds.width, height: view.bounds.height))
        textLabel.text = "점점 아픈데가 많은 대장이"
        textLabel.textColor = UIColor.black
        textLabel.textAlignment = .center
        textLabel.font = UIFont.boldSystemFont(ofSize: 30)

        view.addSubview(textLabel)
    }
}

